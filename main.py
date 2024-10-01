import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests

api_key = '0c0fc036d87dbdf453fcf7f736bf65ed'

def get_weather():
    global city
    global temp
    global desc
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temp_celsius = f"{temp-273.15:.2f}"
        desc = data['weather'][0]['description']
        print(f'Temperature: {temp} K')
        print(f'Description: {desc}')

        city_label.config(text=city.title())
        temperature_label.config(text=temp_celsius + "°C")
        description_label.config(text=desc.title())
        
    else:
        print('Error fetching weather data')
    return data, temp, city





root = tk.Tk()
root.title("Weather App")
root.geometry("900x400")

title = tk.Label(root, text="Weather App", font=("Arial", 20))
title.grid(row=0, column=0)

inputlabel = tk.Label(root, text="Enter City")
inputlabel.grid(row=1, column=0)

city_entry = tk.Entry(root, font=("Arial", 20))
city_entry.grid(row=1, column=1, padx=20, pady=10)

fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 20), command=get_weather)
fetch_button.grid(row=1, column=2, padx=10)

city_label = tk.Label(root, text="", font=("Arial", 30))
city_label.grid(row=2, column=0, columnspan=2, pady=10)

temperature_label = tk.Label(root, text="", font=("Arial", 30))
temperature_label.grid(row=3, column=0, columnspan=2, pady=10)

description_label = tk.Label(root, text="", font=("Arial", 30))
description_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()