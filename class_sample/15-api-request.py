# # uv add requests
# # https://finnhub.io/
# # https://finnhub.io/docs/api/quote


# # build a application to ask user enter the stock they want to buy
# # and check the price of current stock, and notify the user 
# # if cureent price is bigger than the average of (high + low)
# # and tell user how much is different from previous close price if 
# # they buy it now

# import requests

# API_KEY = "dbua5k9r01qv51javdngdbua5k9r01qv51javdo0"

# stock_name = input("Enter the stock symbol you want to buy: ")

# data = requests.get(
#     "https://finnhub.io/api/v1/quote",
#     params={"symbol": stock_name, "token": API_KEY}
# ).json()

# print(data)

# print("Current Price: $", data["c"])
# if data["c"] > (data["h"] + data["l"]) / 2:
#     print("Current price is higher than the average of high and low.")
# else:
#     print("Current price is not higher than the average of high and low.")

# print("Difference from previous close: $", data["c"] - data["pc"])



# # import requests

# # API_KEY = "dbua5k9r01qv51javdngdbua5k9r01qv51javdo0"

# # data = requests.get(
# #     "https://finnhub.io/api/v1/quote",
# #     params={"symbol": "NVDA", "token": API_KEY}
# # ).json()

# # print(data)

# # print("NVIDIA Price: $", data["c"])


