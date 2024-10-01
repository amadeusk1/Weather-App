import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import os  # For debugging paths

api_key = '0c0fc036d87dbdf453fcf7f736bf65ed'

def get_weather(event=None):
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temp_celsius = f"{temp-273.15:.2f}"
        desc = data['weather'][0]['description']

        city_label.config(text=city.title())
        temperature_label.config(text=temp_celsius + "°C")
        description_label.config(text=desc.title())
        
        update_image(desc)  # Update the image based on the description
    else:
        messagebox.showerror("Error", "Error fetching weather data")

def update_image(description):
    description = description.lower()

    try:
        if 'clear' in description:
            img = Image.open("sunny.png")
        elif 'cloud' in description:
            img = Image.open("cloudy.png")
        elif 'rain' in description:
            img = Image.open("rainy.png")
        elif 'snow' in description:
            img = Image.open("snow.png")
        elif 'storm' in description:
            img = Image.open("storm.png")
        else:
            img = Image.open("default.png")  # Default image if description doesn't match
        
        img = img.resize((150, 150), Image.Resampling.LANCZOS)  # Larger image for better visibility
        weather_img = ImageTk.PhotoImage(img)
        
        # Assign image to label and keep a reference to avoid garbage collection
        image_label.config(image=weather_img)
        image_label.image = weather_img
        
    except Exception as e:
        print(f"Error loading image: {e}")

# Function to change button color on hover
def on_enter(e):
    fetch_button['background'] = "#cccccc"
def on_leave(e):
    fetch_button['background'] = button_bg

root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")

# Light theme colors
bg_color = "#f9f9f9"
fg_color = "#333333"
button_bg = "#eeeeee"
button_fg = "#333333"
entry_bg = "#ffffff"
entry_fg = "#333333"
border_color = "#cccccc"

root.configure(bg=bg_color)

# Title with larger font and padding
title = tk.Label(root, text="Weather App", font=("Helvetica", 28, "bold"), bg=bg_color, fg=fg_color)
title.grid(row=0, column=0, columnspan=2, pady=20)

# City entry field, center aligned
city_entry = tk.Entry(root, font=("Helvetica", 18), bg=entry_bg, fg=entry_fg, insertbackground=entry_fg, justify='center', bd=2, relief='solid')
city_entry.grid(row=0, column=3, columnspan=2, padx=20, pady=10, ipady=5)
city_entry.bind('<Return>', get_weather)  # Bind the Enter key to the get_weather function

"""
# Fetch button with rounded corners and hover effect
fetch_button = tk.Button(root, text="Get Weather", font=("Helvetica", 18), bg=button_bg, fg=button_fg, bd=2, relief="solid", padx=20, pady=10)
fetch_button.grid(row=0, column=5, columnspan=2, pady=20)
fetch_button.bind("<Enter>", on_enter)
fetch_button.bind("<Leave>", on_leave)
fetch_button.config(command=get_weather)
"""

# City label, center aligned
city_label = tk.Label(root, text="", font=("Helvetica", 28, "bold"), bg=bg_color, fg=fg_color)
city_label.grid(row=1, column=0, columnspan=2, pady=10)

# Temperature label, center aligned
temperature_label = tk.Label(root, text="", font=("Helvetica", 24), bg=bg_color, fg=fg_color)
temperature_label.grid(row=4, column=0, columnspan=2, pady=10)

# Description label, center aligned
description_label = tk.Label(root, text="", font=("Helvetica", 20), bg=bg_color, fg=fg_color)
description_label.grid(row=3, column=0, columnspan=2, pady=10)

# Weather image label, center aligned
image_label = tk.Label(root, bg=bg_color)
image_label.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
