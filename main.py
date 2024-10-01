import tkinter as tk
from tkinter import messagebox
import requests

api_key = '0c0fc036d87dbdf453fcf7f736bf65ed'
city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')





root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.mainloop()