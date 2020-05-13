# another tkinter test project
# based on "How to Program a GUI Application (with Python Tkinter)!" by Keith Galli
# link: https://www.youtube.com/watch?v=D8-snVfekto
#
# this time learning to build an application (weather app) with multiple frames and API use

import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature(F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '4d3fb0d0d1ba06a5a16ef7586d2a006c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

root.title('weather by carter')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='orange', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('consolas', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('consolas', 20), fg='red', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='orange', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='yellow', font=('consolas', 20), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
