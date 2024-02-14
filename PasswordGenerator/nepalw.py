from tkinter import *
import requests

root = Tk()
root.geometry("400x400")
def get_air_quality(location="Nepal"):
    # base_url =
    params = {
        "country": location,
        "limit": 5  # You can adjust the limit as per your requirement
    }
    response = requests.get("https://api.openaq.org/v1/measurements")

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        for result in results:
            city = result.get("city", "Unknown")
            parameter = result.get("parameter", "Unknown")
            value = result.get("value", "Unknown")
            unit = result.get("unit", "Unknown")
            print(f"City: {city}, Parameter: {parameter}, Value: {value} {unit}")
    else:
        print("Failed to fetch air quality data.")


# Call the function to get air quality information for Nepal
# get_air_quality("NP")

country = Entry(root)
country.grid(row=0, column=0, stick= W+E+N+S)

country_btn = Button(root, text="find weather", command= get_air_quality("Np"))
country_btn.grid(row=0, column=1, sticky= W+E+N+S)

root.mainloop()
