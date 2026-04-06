product_prices = [20, 10, 30, 20, 33, 37, 77, 88]
total_price = 0

for i, price in enumerate(product_prices):
    print(f"Product price is ({i}): {price}")
    total_price += price

print(f"{total_price = }")
average = total_price / len(product_prices)

print(f"{average = }")

# print(sum(product_prices) / len(product_prices))
