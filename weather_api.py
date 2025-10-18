# weather_api.py
"""
Simple OpenWeatherMap wrapper + JSON file cache.
Provides get_current_weather(city) and get_forecast(city).
"""

import requests
import time
import json
from pathlib import Path
from dateutil import tz

CACHE_FILE = Path("weather_cache.json")
CACHE_TTL = 300  # seconds to keep cache (5 minutes)

class WeatherAPIError(Exception):
    pass

class WeatherAPI:
    def __init__(self, api_key, units="metric", lang="en"):
        self.api_key = api_key
        self.base = "https://api.openweathermap.org/data/2.5"
        self.units = units
        self.lang = lang
        self._cache = self._load_cache()

    def _load_cache(self):
        if CACHE_FILE.exists():
            try:
                return json.loads(CACHE_FILE.read_text())
            except Exception:
                return {}
        return {}

    def _save_cache(self):
        CACHE_FILE.write_text(json.dumps(self._cache))

    def _cache_get(self, key):
        entry = self._cache.get(key)
        if not entry:
            return None
        if time.time() - entry["ts"] > CACHE_TTL:
            self._cache.pop(key, None)
            return None
        return entry["value"]

    def _cache_set(self, key, value):
        self._cache[key] = {"ts": time.time(), "value": value}
        self._save_cache()

    def _request(self, path, params):
        url = f"{self.base}/{path}"
        params.update({"appid": self.api_key, "units": self.units, "lang": self.lang})
        try:
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            raise WeatherAPIError(f"Network/API error: {e}") from e

    def get_current_weather(self, city):
        key = f"current:{city}:{self.units}:{self.lang}"
        cached = self._cache_get(key)
        if cached:
            return cached

        data = self._request("weather", {"q": city})
        # Normalize response to useful fields
        out = {
            "city": f"{data.get('name')}, {data.get('sys', {}).get('country')}",
            "weather": data["weather"][0]["description"].capitalize(),
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"].get("speed"),
            "timestamp": data.get("dt"),
        }
        self._cache_set(key, out)
        return out

    def get_forecast(self, city, days=3):
        # OpenWeatherMap 5-day/3-hour forecast endpoint "forecast"
        key = f"forecast:{city}:{days}:{self.units}:{self.lang}"
        cached = self._cache_get(key)
        if cached:
            return cached

        data = self._request("forecast", {"q": city})
        # We aggregate into daily summaries for next `days` days
        from collections import defaultdict
        import datetime

        tz_local = tz.tzlocal()

        daily = defaultdict(list)
        for item in data.get("list", []):
            dt = datetime.datetime.utcfromtimestamp(item["dt"]).replace(tzinfo=tz.tzutc()).astimezone(tz_local)
            day = dt.date().isoformat()
            temp = item["main"]["temp"]
            weather = item["weather"][0]["description"]
            wind = item["wind"]["speed"]
            daily[day].append({"dt": item["dt"], "temp": temp, "weather": weather, "wind": wind})

        sorted_days = sorted(daily.items())
        summary = []
        for day_iso, entries in sorted_days[:days]:
            temps = [e["temp"] for e in entries]
            weathers = [e["weather"] for e in entries]
            winds = [e["wind"] for e in entries]
            summary.append({
                "date": day_iso,
                "temp_min": min(temps),
                "temp_max": max(temps),
                "weather": max(set(weathers), key=weathers.count).capitalize(),
                "wind_avg": sum(winds)/len(winds),
            })
        self._cache_set(key, summary)
        return summary