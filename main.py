import yfinance as yf
import pandas as pd

# Define the stock ticker for Nvidia
ticker = "NVDA"

# Define the start and end dates for the data retrieval
start_date = "2024-06-10"
end_date = "2024-10-08"  # Today's date

# Fetch the data
nvidia_data = yf.download(ticker, start=start_date, end=end_date)

# Display the retrieved data
print(nvidia_data)
