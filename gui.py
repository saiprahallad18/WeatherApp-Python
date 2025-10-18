# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import os
from weather_api import WeatherAPI, WeatherAPIError

class WeatherApp(tk.Tk):
    def __init__(self, api_key):
        super().__init__()
        self.title("Thinker Weather")
        self.geometry("720x600")
        self.api = WeatherAPI(api_key)

        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        self.city_var = tk.StringVar(value="Hyderabad,IN")
        ttk.Label(frm, text="City:").grid(row=0, column=0, sticky="w")
        self.city_entry = ttk.Entry(frm, textvariable=self.city_var, width=30)
        self.city_entry.grid(row=0, column=1, sticky="w")
        ttk.Button(frm, text="Get Weather", command=self.fetch).grid(row=0, column=2, padx=8)

        self.output = tk.Text(frm, height=12, width=60, state="disabled", wrap="word")
        self.output.grid(row=1, column=0, columnspan=3, pady=10)

    def fetch(self):
        city = self.city_var.get().strip()
        if not city:
            messagebox.showinfo("Input", "Please enter a city name.")
            return
        try:
            cur = self.api.get_current_weather(city)
            fc = self.api.get_forecast(city, days=3)
            text = []
            text.append(f"Weather for: {cur['city']}\n")
            text.append(f"{cur['weather']}\n")
            text.append(f"Temp: {cur['temp']}° (feels like {cur['feels_like']}°)\n")
            text.append(f"Humidity: {cur['humidity']}%\n")
            text.append(f"Wind speed: {cur['wind_speed']} m/s\n\n")
            text.append("3-day forecast:\n")
            for d in fc:
                text.append(f"{d['date']}: {d['weather']}, {d['temp_min']}° — {d['temp_max']}°, wind {d['wind_avg']:.1f} m/s\n")
            self.output.config(state="normal")
            self.output.delete("1.0", tk.END)
            self.output.insert("1.0", "".join(text))
            self.output.config(state="disabled")
        except WeatherAPIError as e:
            messagebox.showerror("Error", f"Could not get weather: {e}")

if __name__ == "__main__":
    key = os.getenv("OWM_API_KEY")
    #key = "REPLACE WITH YOUR API KEY"
    if not key:
        print("Set OWM_API_KEY environment variable with your OpenWeatherMap API key.")
    else:
        app = WeatherApp(key)
        app.mainloop()