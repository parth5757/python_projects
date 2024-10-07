import yfinance as yf
import datetime

# import pandas as pd


def get_yearly_dividends(stocks):
    results = []

    for stock in stocks:
        name = stock["name"]
        amount = stock["amount"]
        purchase_date = datetime.datetime.strptime(stock["purchase_date"], "%Y-%m-%d")
        ticker = yf.Ticker(name)
        dividends = ticker.dividends

        # Convert the dividend dates to timezone-naive if they are timezone-aware
        if dividends.index.tz is not None:
            dividends.index = dividends.index.tz_convert(None)

        # Filter dividends paid since the purchase date
        dividends_since_purchase = dividends[dividends.index >= purchase_date]

        # Calculate the total dividends received since purchase
        total_dividends = dividends_since_purchase.sum()
        years_held = datetime.datetime.now().year - purchase_date.year
        yearly_dividend = (
            total_dividends / years_held if years_held > 0 else total_dividends
        )

        results.append(
            {
                "name": name,
                "years_held": years_held,
                "total_dividends": total_dividends,
                "yearly_dividend": yearly_dividend,
            }
        )

    return results


def main():
    stocks = []
    n = int(input("Enter the number of stocks: "))

    for _ in range(n):
        name = input("Enter the stock name: ")
        amount = float(input(f"Enter the amount invested in {name}: "))
        purchase_date = input(f"Enter the purchase date of {name} (YYYY-MM-DD): ")

        stocks.append({"name": name, "amount": amount, "purchase_date": purchase_date})

    results = get_yearly_dividends(stocks)

    for result in results:
        print(
            f"Stock: {result['name']}, Years Held: {result['years_held']}, Total Dividends: ₹{result['total_dividends']:.2f}, Yearly Dividend: ₹{result['yearly_dividend']:.2f}"
        )


if __name__ == "__main__":
    main()


# import yfinance as yf
# import datetime
# import pandas as pd

# def get_stock_price_on_date(ticker, date):
#     # Try to fetch historical market data for the stock
#     hist = ticker.history(start=date, end=date)
#     # If no data is found for the exact date, try to get the nearest date
#     if hist.empty:
#         # Try to get data for the previous day if the market was closed on the given date
#         hist = ticker.history(start=date, end=pd.to_datetime(date) + pd.DateOffset(1))
#         if hist.empty:
#             raise ValueError(f"No data available for {ticker} on {date} or the nearest available date")
#     return hist['Close'][0]

# def get_yearly_dividends(stocks):
#     results = []

#     for stock in stocks:
#         name = stock['name']
#         purchases = stock['purchases']
#         ticker = yf.Ticker(name)
#         total_amount = 0
#         total_shares = 0

#         for purchase in purchases:
#             purchase_date = datetime.datetime.strptime(purchase['date'], '%Y-%m-%d')
#             shares = purchase['shares']
#             try:
#                 price_on_date = get_stock_price_on_date(ticker, purchase['date'])
#             except ValueError as e:
#                 print(e)
#                 continue  # Skip this purchase if no data is available

#             amount_invested = shares * price_on_date
#             total_amount += amount_invested
#             total_shares += shares

#             # Add dividends per purchase
#             dividends = ticker.dividends
#             if dividends.index.tz is not None:
#                 dividends.index = dividends.index.tz_convert(None)
#             dividends_since_purchase = dividends[dividends.index >= purchase_date]
#             total_dividends = dividends_since_purchase.sum() * shares
#             years_held = datetime.datetime.now().year - purchase_date.year
#             yearly_dividend = total_dividends / years_held if years_held > 0 else total_dividends

#             results.append({
#                 'name': name,
#                 'purchase_date': purchase_date,
#                 'shares': shares,
#                 'total_dividends': total_dividends,
#                 'yearly_dividend': yearly_dividend
#             })

#     return results

# def main():
#     stocks = []
#     n = int(input("Enter the number of stocks: "))

#     for _ in range(n):
#         name = input("Enter the stock name: ")
#         purchases = []
#         more_purchases = True

#         while more_purchases:
#             purchase_date = input(f"Enter the purchase date of {name} (YYYY-MM-DD): ")
#             shares = int(input(f"Enter the number of shares purchased on {purchase_date}: "))
#             purchases.append({
#                 'date': purchase_date,
#                 'shares': shares
#             })
#             more_purchases = input("Do you have more purchases for this stock? (yes/no): ").lower() == 'yes'

#         stocks.append({
#             'name': name,
#             'purchases': purchases
#         })

#     results = get_yearly_dividends(stocks)

#     for result in results:
#         print(f"Stock: {result['name']}, Purchase Date: {result['purchase_date']}, Shares: {result['shares']}, Total Dividends: ₹{result['total_dividends']:.2f}, Yearly Dividend: ₹{result['yearly_dividend']:.2f}")

# if __name__ == "__main__":
#     main()
