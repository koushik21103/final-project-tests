import requests
symbol=input("Enter the stock symbol:").upper()
api_key = "S40J0DAUT1EI56JN"
#y=input("Enter year:")
#m=input("Enter month:")
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}"
r = requests.get(url)
data = r.json()

#print(json.dumps(data, indent=4))

time_series = data["Time Series (Daily)"]

#Iterate through the date and "4. close" attributes
'''for date, values in time_series.items():
    close_price = values["4. close"]
    print(f"Date: {date}, Close Price: {close_price}")'''

print(time_series)
    
    
    
    