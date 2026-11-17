# https://finnhub.io/
# https://finnhub.io/docs/api/quote

import requests

API_KEY = "dbua5k9r01qv51javdngdbua5k9r01qv51javdo0"

data = requests.get(
    "https://finnhub.io/api/v1/quote",
    params={"symbol": "NVDA", "token": API_KEY}
).json()

print("NVIDIA Price: $", data["c"])