import requests
import sys
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image


def pobranie_lokalizacji():
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={miasto_entry.get()}")
    nr_miasto = resp.json()[0]['woeid']
    resp2 = requests.get(f"https://www.metaweather.com/api/location/{nr_miasto}/")
    pogoda = resp2.json()['consolidated_weather'][0]

    temp_wynik_label.configure(text=f"{pogoda['the_temp']}")
    cis_wynik_label.configure(text=f"{pogoda['air_pressure']}")

    rys = "slonce_chmura.jpg"
    img = ImageTk.PhotoImage(Image.open(rys))#.resize((140, 120), Image.ANTIALIAS))

    panel = tkinter.Label(master=root, height = 160, width =200, background = "black", image=img)
    panel.grid(row=7, columnspan=2)
    panel.image = img


root = tkinter.Tk()
root.title("Prognoza pogody")
#miasto = input("Poddaj miasto: ")

back = tkinter.Frame(master=root, width=80, height=80) #bg='black')
back.grid()

miasto_label = tkinter.Label(master=root, text='Miasto')
miasto_label.grid(row=0, column=0)

miasto_entry = tkinter.Entry(master=root)
miasto_entry.grid(row=0, column=1, padx=40)

button = tkinter.Button(master=root, text="Sprawdź pogodę", command=pobranie_lokalizacji)
button.grid(row=2, column=1)

temp_label = tkinter.Label(master=root, text='Temperatura:')
temp_label.grid(row=4, column=0)

temp_wynik_label = tkinter.Label(master=root, text='---')
temp_wynik_label.grid(row=4, column=1)

cis_label = tkinter.Label(master=root, text='Ciśnienie')
cis_label.grid(row=5, column=0)

cis_wynik_label = tkinter.Label(master=root, text='---')
cis_wynik_label.grid(row=5, column=1)


root.mainloop()
