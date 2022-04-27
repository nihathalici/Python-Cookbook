# 1.1.Unpacking-a-Sequence-into-Separate-Variables.py

p = (4, 5)
x, y = p

print(x)
print(y)

###

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

print(name)
print(date)

###

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)

###

s = 'Hello'
a, b, c, d, e = s
print(a)

###

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares)
print(price) 
