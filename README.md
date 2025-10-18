# 🌦️ Thinker Weather

A simple, tinker-friendly Python weather app that works both in **CLI** and **GUI** modes.  
It uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch real-time weather and 3-day forecasts, with a lightweight JSON cache to reduce API calls.


## 🚀 Features

- 🧠 Reusable `WeatherAPI` wrapper (handles caching, errors, and normalization)
- 💻 Command-line interface (CLI) with neat text formatting
- 🪟 Desktop GUI using `Tkinter`
- 🗂️ Local JSON cache to reduce repeated API requests
- 🌍 Supports different units and languages via OpenWeatherMap parameters



## 📁 Project Structure


.
├── weather_api.py   # API wrapper + caching logic
├── gui.py           # Tkinter desktop app
├── cli.py           # Command-line interface
├── weather_cache.json  # Auto-generated cache file
└── README.md


## 🧰 Requirements

**Python 3.8+** is recommended.

### Install dependencies:
bash
pip install requests python-dateutil




## 🔑 Setup

1. Get your **OpenWeatherMap API key**:
   → [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up)

2. Set it as an environment variable:

   bash
   export OWM_API_KEY="your_api_key_here"   # macOS / Linux
   setx OWM_API_KEY "your_api_key_here"     # Windows (PowerShell)
   



## 🧩 Usage

### 🖥️ GUI Mode

Run the Tkinter app:

bash
python gui.py


Enter a city name (e.g., `Hyderabad,IN`) and click **Get Weather**
to see current conditions and a 3-day forecast.

### 🧾 CLI Mode

Run the app from your terminal:

bash
python cli.py "Bengaluru,IN"


Add flags:

bash
--no-forecast    # Fetch only current weather
--key YOUR_KEY   # Provide API key directly (optional)


Example:

bash
python cli.py "London" --no-forecast




## 🧠 Example Output (CLI)


Weather for: Hyderabad, IN
  Clear sky
  Temp: 30.2° (feels like 33.0°)
  Humidity: 45%
  Wind speed: 2.5 m/s

3-day forecast:
  2025-10-18: Clouds, 28° — 33°, wind avg 3.1 m/s
  2025-10-19: Rain, 25° — 31°, wind avg 4.2 m/s
  2025-10-20: Clear, 26° — 32°, wind avg 3.5 m/s




## 🧩 Technical Details

* **Cache TTL:** 5 minutes
* **Cache file:** `weather_cache.json`
* **Endpoints used:**

  * `/data/2.5/weather`
  * `/data/2.5/forecast`



## 🐞 Error Handling

If the API fails or network is unavailable, the app will:

* Raise a `WeatherAPIError`
* Display a friendly error popup (in GUI) or print a message (in CLI)



## 🧑‍💻 Author

**Sai Prahallad**
Built with Python, curiosity, and a bit of cloud data ☁️



## 📜 License

This project is open-source and available under the **MIT License**.

