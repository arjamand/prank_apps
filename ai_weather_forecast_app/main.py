# 2023-08-06 10:52:31

import tkinter as tk
from tkinter import ttk
import time

def show_loading_popup():
    loading_popup = tk.Toplevel(window)
    loading_popup.title("Loading")
    loading_popup.geometry("300x120")

    phrases = ["Searching location...", "Analyzing the clouds...", "Gathering data...", "Preparing forecast..."]
    
    status_label = tk.Label(loading_popup, text="", padx=50, pady=10)
    status_label.pack()

    progress = ttk.Progressbar(loading_popup, style="smooth.Horizontal.TProgressbar", length= 200, mode="determinate")
    progress.pack()

    progress["value"] = 0

    for index, phrase in enumerate(phrases, start=1):
        status_label.config(text=phrase, bg="white")
        for _ in range(10):  # Update in smaller increments
            progress["value"] += index
            loading_popup.update_idletasks()
            time.sleep(0.1)  # Smaller delay for smoother animation
        time.sleep(0.5)
    loading_popup.destroy()
    show_result_popup()


    # for index, phrase in enumerate(phrases, start=1):
    #     status_label.config(text=phrase,bg = "white")
    #     progress["value"] = index
    #     loading_popup.update_idletasks()
    #     time.sleep(2)
    #     status_label.config(text="",bg = "white")
    #     # time.sleep(2)  # Reduced delay for smoother animation
    
    # loading_popup.destroy()
    # show_result_popup()

def show_result_popup():
    result_popup = tk.Toplevel(window)
    result_popup.title("Result")
    result_popup.geometry("250x100")
    result_label = tk.Label(result_popup, text="idk, look out the window !",pady=10)
    result_label.pack()
    ok_button = tk.Button(result_popup, text="   OK   ", command=result_popup.destroy)
    ok_button.pack()

def fetch_weather_forecast():
    show_loading_popup()

window = tk.Tk()
window.title("AI Weather Forecast!")
window.minsize(350, 160)

tk.Label(window, text="Enter your Location:", font=("Arial", 10, "bold"), pady=10).pack()

location_input = tk.Entry(window)
location_input.pack()

# Adding spacing between Entry and Button
spacing_label = tk.Label(window, text="", pady=5)
spacing_label.pack()

fetch_button = tk.Button(window, text="Fetch Forecast", command=fetch_weather_forecast)
fetch_button.pack()

window.mainloop()
