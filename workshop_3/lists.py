product_prices = [20, 10, 30, 20, 33, 37, 77, 88]

print(type(product_prices))
print(f"{len(product_prices) = }")
print(product_prices)

print(product_prices[0])
print(product_prices[1])
print(product_prices[-1])
print(product_prices[-2])

print("Middle element(s):")
mid_point = len(product_prices) // 2
if len(product_prices) % 2 == 0:
    print(product_prices[mid_point - 1], product_prices[mid_point])
    print((product_prices[mid_point - 1] + product_prices[mid_point]) / 2)
else:
    print(product_prices[mid_point])


# product_prices[0] = 22
product_prices[0] += 1

print(product_prices[0])


product_prices.pop(0)
print(product_prices)

product_prices.append(65)
print(product_prices)


product_prices.insert(0, 65)
print(product_prices)

product_prices.insert(len(product_prices) // 2, 65)
print(product_prices)

product_prices.sort()
print(product_prices)
product_prices.reverse()
print(product_prices)