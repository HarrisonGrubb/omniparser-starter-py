import json
import os
import pandas as pd 
import statistics

def calculate_latest_closing_price_from_json(location):
    with open(location, 'r') as reader:
        contents = reader.read()
        #print(contents)

    data = json.loads(contents)
    daily_data = data["Time Series (Daily)"]
    #need to get last post
if __name__ == "__main__":
    
    path = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")
    calculate_latest_closing_price_from_json(path)