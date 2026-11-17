
import requests

url = "http://127.0.0.1:5000/value"

# GET: Read current value
response = requests.get(url)
print("GET:", response.json())

# POST: Change value to 100
response = requests.post(url, json={"value": 100})
print("POST:", response.json())

# GET again: Verify new value
response = requests.get(url)
print("GET again:", response.json())
