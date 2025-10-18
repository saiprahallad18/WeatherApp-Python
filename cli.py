# cli.py
import argparse
from weather_api import WeatherAPI, WeatherAPIError
import os
import textwrap

def pretty_current(w):
    return textwrap.dedent(f"""
    Weather for: {w['city']}
      {w['weather']}
      Temp: {w['temp']}° (feels like {w['feels_like']}°)
      Humidity: {w['humidity']}%
      Wind speed: {w['wind_speed']} m/s
    """)

def pretty_forecast(forecast):
    lines = ["3-day forecast:"]
    for d in forecast:
        lines.append(f"  {d['date']}: {d['weather']}, {d['temp_min']}° — {d['temp_max']}°, wind avg {d['wind_avg']:.1f} m/s")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Tinkerable Python Weather App (CLI)")
    parser.add_argument("city", help="City name, e.g. 'Bengaluru,IN' or 'London'")
    parser.add_argument("--key", help="OpenWeatherMap API key (or set OWM_API_KEY env)")
    parser.add_argument("--no-forecast", action="store_true", help="Don't fetch forecast")
    args = parser.parse_args()

    api_key = args.key or os.getenv("OWM_API_KEY")
    if not api_key:
        print("ERROR: Provide API key with --key or set OWM_API_KEY env variable.")
        return

    api = WeatherAPI(api_key)
    try:
        cur = api.get_current_weather(args.city)
        print(pretty_current(cur))
        if not args.no_forecast:
            fc = api.get_forecast(args.city, days=3)
            print(pretty_forecast(fc))
    except WeatherAPIError as e:
        print("Failed:", e)

if __name__ == "__main__":
    main()