import requests


def get_air_quality(location="NP", city="Kathmandu"):
    base_url = "https://api.openaq.org/v1/measurements"
    params = {
        "country": location,
        "city": city,
        "limit": 5  # You can adjust the limit as per your requirement
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        for result in results:
            parameter = result.get("parameter", "Unknown")
            value = result.get("value", "Unknown")
            unit = result.get("unit", "Unknown")
            print(f"Parameter: {parameter}, Value: {value} {unit}")
    else:
        print("Failed to fetch air quality data.")


# Call the function to get air quality information for Kathmandu, Nepal
get_air_quality(location="NP", city="Kathmandu")
