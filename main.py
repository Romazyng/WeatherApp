import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    celc = (weather['main']['temp'] - 32) * 5 / 9
    celc_v2 = round(celc, 1)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = celc_v2
        feels_like = round((weather['main']['feels_like'] - 32) * 5 / 9, 1)

        final_str = 'City: %s \nConditions: %s \nTemperature(°C): %s \nFeels like: %s' % (name, desc, temp, feels_like)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str

def test_function(entry):
    print('This is the entry:', entry)


def get_weather(city):
    weather_key = '7550393428f77def36b6c67a4ec3b08c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 13))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 13), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 16))
label.place(relwidth=1, relheight=1)

root.mainloop()


