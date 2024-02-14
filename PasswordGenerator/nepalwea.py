import requests
import tkinter as tk

def get_air_quality(country_code):
    # OpenAQ API endpoint to fetch air quality data for a specific country
    url = f"https://api.openaq.org/v1/latest?country={country_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract relevant information
        results = data['results']
        air_quality_info = []
        for result in results:
            location = result['location']
            parameter = result['measurements'][0]['parameter']
            value = result['measurements'][0]['value']
            unit = result['measurements'][0]['unit']
            air_quality_info.append(f"Location: {location}, Parameter: {parameter}, Value: {value} {unit}")

        return air_quality_info

    except requests.exceptions.RequestException as e:
        return [f"Error fetching data: {e}"]

def display_air_quality():
    country_code = country_entry.get()
    air_quality_info = get_air_quality(country_code)

    # Clear any previous output
    output_text.delete(1.0, tk.END)

    # Display air quality information
    for info in air_quality_info:
        output_text.insert(tk.END, info + '\n')


# Create a Tkinter window
root = tk.Tk()
root.title("Air Quality Checker")
root.geometry("600x300")

# Create and pack widgets
tk.Label(root, text="Enter country code:").pack()
country_entry = tk.Entry(root)
country_entry.pack()

fetch_button = tk.Button(root, text="Fetch Air Quality", command=display_air_quality)
fetch_button.pack()

output_text = tk.Text(root, height=10, width=90)
output_text.pack()

# Run the Tkinter event loop
root.mainloop()
