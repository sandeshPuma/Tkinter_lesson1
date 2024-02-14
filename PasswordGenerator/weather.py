from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title("weather APP")
root.iconbitmap('D:/python/new Lesson/icon/apple.ico')
root.geometry("600x100")


def ziplookup():  # create a zipcode lookup function
    # zip.get()
    # ziplabel = Label(root, text = zip.get())
    # ziplabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zip.get() +"&date=2024-02-13&distance=25&API_KEY=5A79491B-FEA0-4881-ADD9-E796569702FF")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Group":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000 "
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000 "

        root.configure(background=weather_color)
        my_label = Label(root, text=city + 'Air Quality ' + str(quality) + " " + category, font=('Helvetica', 20),
                         background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error Occurred...."


# https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2024-02-13&distance=25&API_KEY=5A79491B-FEA0-4881-ADD9-E796569702FF




zip = Entry(root)
zip.grid(row=0, column=0, stick= W+E+N+S)

zip_btn = Button(root, text="Lookup Zipcode", command= ziplookup)
zip_btn.grid(row=0, column=1, stick= W+E+N+S)

root.mainloop()

