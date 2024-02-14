import json
import requests

api = requests.get("https://api.openaq.org/v1/measurements")

parsed_data = json.loads(api)
results = parsed_data['results']

for result in results:
    location = result['location']
    parameter = result['parameter']
print(result)
