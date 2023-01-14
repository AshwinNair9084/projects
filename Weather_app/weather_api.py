
from tkinter import *
import requests
import json

root=Tk()
root.geometry("650x200")

def zipcode():
    try:
        data = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+str(zipentry.get())+"&distance=25&API_KEY=C4DCCD9C-4F9A-40AF-84D9-FDD64F6430BD")
        data = json.loads(data.content)
        city = data[0]['ReportingArea']
        quality = data[0]['AQI']
        airtype = data[0]['Category']['Name']
        if airtype == "Good":
            color = "#00e400"

        elif airtype == "Moderate":
            color = "#ffff00"
        elif airtype == "Unhealthy for Sensitive Groups":
            color = "#ff7e00"
        elif airtype == "Unhealthy":
            color = "#ff0000"
        elif airtype == "Very Unhealthy":
            color = "#8f3f97"
        elif airtype == "Hazardous":
            color = "#7e0023"

        Label(root, text=str(city) + ", Ozone Quallity : " + str(quality) + "\n" + str(airtype),
              background=color, font=('arial', 20, 'bold')).grid(row = 2, column=1)
        ziplabel.config(background=color)
        zipbutton.config(bg=color)
        root.config(background=color)
        zipentry.delete(0,END)

    except:
        print("error")

ziplabel = Label(root, text="Enter your zipcode : ")
ziplabel.grid(row = 0, column = 0)
zipentry = Entry(root)
zipentry.grid(row = 0, column = 1)

zipbutton = Button(root, text="Get weather", command=zipcode)
zipbutton.grid(row=1, column=0)

root.mainloop()