import yfinance as yf

def get_stock_data(stock_symbol, start_date, end_date):
    # 獲取股票歷史數據
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

# 範例：獲取蘋果公司過去1年的股票數據
stock_data = get_stock_data("AAPL", "2023-04-01", "2024-04-01")
print(stock_data.head())
