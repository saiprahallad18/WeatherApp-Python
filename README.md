---
# 🌦️ Thinker Weather

A simple, tinker-friendly Python weather app that works in both **CLI** and **GUI** modes.  
It uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch real-time weather and 3-day forecasts, with a local JSON cache to reduce API calls.

---

## 🚀 Features
- 🧠 Reusable `WeatherAPI` class with caching and error handling  
- 💻 Command-line interface (CLI) for quick access  
- 🪟 Desktop GUI using Tkinter  
- 🗂️ JSON file cache to avoid redundant requests  
- 🌍 Supports different units and languages  

---

## 📁 Project Structure
```

.
├── weather_api.py        # API wrapper + caching logic
├── gui.py                # Tkinter desktop app
├── cli.py                # Command-line interface
├── weather_cache.json    # Auto-created cache file
└── README.md

````

---

## 🧰 Requirements
**Python 3.8+** is recommended.

Install dependencies:
```bash
pip install requests python-dateutil
````

---

## 🔑 Setup

1. Get a free **OpenWeatherMap API key**:
   [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up)

2. Set it as an environment variable:

   ```bash
   export OWM_API_KEY="your_api_key_here"   # macOS / Linux
   setx OWM_API_KEY "your_api_key_here"     # Windows (PowerShell)
   ```

---

## 🖥️ GUI Usage

Run the GUI version:

```bash
python gui.py
```

Enter a city name (e.g., `Hyderabad,IN`) and click **Get Weather**
to see current weather and a 3-day forecast.

---

## 💻 CLI Usage

Run the app from the terminal:

```bash
python cli.py "Bengaluru,IN"
```

Optional flags:

```bash
--no-forecast    # Skip forecast
--key YOUR_KEY   # Provide API key directly
```

Example:

```bash
python cli.py "London" --no-forecast
```

---

## 📊 Example Output (CLI)

```
Weather for: Hyderabad, IN
  Clear sky
  Temp: 30.2° (feels like 33.0°)
  Humidity: 45%
  Wind speed: 2.5 m/s

3-day forecast:
  2025-10-18: Clouds, 28° — 33°, wind avg 3.1 m/s
  2025-10-19: Rain, 25° — 31°, wind avg 4.2 m/s
  2025-10-20: Clear, 26° — 32°, wind avg 3.5 m/s
```

---

## ⚙️ Technical Details

* **Cache TTL:** 5 minutes
* **Cache file:** `weather_cache.json`
* **API endpoints:**

  * `/data/2.5/weather`
  * `/data/2.5/forecast`

---

## 🧩 Error Handling

If something goes wrong (invalid city, network issue, API failure):

* A `WeatherAPIError` is raised
* GUI shows a popup error message
* CLI prints a clear error message

---

## 👨‍💻 Author

**Sai Prahallad**
Built with Python, curiosity, and a bit of cloud data ☁️

---

## 🆓 License

This project is **free to use, modify, and share** for any purpose — personal, educational, or commercial.  
No attribution is required, but it’s always appreciated if you mention the original author.

You may:
- Use this code in your own projects  
- Modify or extend it  
- Distribute it freely  

This software is provided *as is*, without any warranty or guarantee of fitness for a particular purpose.
