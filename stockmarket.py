stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("Enter stock names and quantities. Type 'done' to finish.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\nYour Portfolio Summary:\n")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save == "yes":
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print(f"Portfolio saved to {filename}")
