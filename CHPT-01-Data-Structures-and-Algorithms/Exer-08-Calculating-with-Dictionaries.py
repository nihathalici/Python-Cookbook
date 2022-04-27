# 1.8.Calculating-with-Dictionaries.py


prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)
print(prices_sorted)

###

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
print(max(prices_and_names))  # ValueError

###

print( min(prices, key=lambda k: prices[k]) )
print( max(prices, key=lambda k: prices[k]) )

###

min_value = prices[ min(prices, key=lambda k: prices[k]) ]
print(min_value)


prices = { 'AAA' : 45.23, 'ZZZ' : 45.23}

print( min(zip(prices.values(), prices.keys())) )

print( max(zip(prices.values(), prices.keys())) )
