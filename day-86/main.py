# 86.Day 86: Weather App UI (Dummy Data)
# Create a UI for Weather App with city input.
# Display static/dummy temperature, humidity, and weather condition.

import tkinter as tk
from tkinter import ttk

# Dummy weather data
DUMMY_WEATHER = {
    "temperature": "28°C",
    "humidity": "65%",
    "condition": "Sunny"
}

# Function to simulate data display
def show_weather():
    city = city_entry.get()
    if city.strip():
        temperature_label.config(text=f"Temperature: {DUMMY_WEATHER['temperature']}")
        humidity_label.config(text=f"Humidity: {DUMMY_WEATHER['humidity']}")
        condition_label.config(text=f"Condition: {DUMMY_WEATHER['condition']}")
        city_label.config(text=f"Weather in {city.title()}")

# GUI setup
root = tk.Tk()
root.title("Weather App UI")
root.geometry("300x300")
root.configure(bg="#f0f8ff")

# Title
title = ttk.Label(root, text="Weather App", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# City input
city_entry = ttk.Entry(root, width=25)
city_entry.pack(pady=10)

# Show button
show_btn = ttk.Button(root, text="Show Weather", command=show_weather)
show_btn.pack(pady=5)

# Weather info labels
city_label = ttk.Label(root, text="", font=("Helvetica", 12))
city_label.pack(pady=5)

temperature_label = ttk.Label(root, text="", font=("Helvetica", 11))
temperature_label.pack()

humidity_label = ttk.Label(root, text="", font=("Helvetica", 11))
humidity_label.pack()

condition_label = ttk.Label(root, text="", font=("Helvetica", 11))
condition_label.pack()

# Run the app
root.mainloop()
