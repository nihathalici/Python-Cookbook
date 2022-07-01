# Exer-08-Interacting-with-a -Relational-Database

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),]

import sqlite3
db = sqlite3.connect('database.db')
c = db.cursor()
c.execute('CREATE TABLE portfolio (symbol text, shares integer, price real)')
db.commit()

c.executemany('INSERT INTO portfolio VALUES (?,?,?)', stocks)
db.commit()

for row in db.execute('SELECT * FROM portfolio'):
    print(row)

min_price = 100
for row in db.execute('SELECT * FROM portfolio WHERE price >= ?',
                      (min_price,)):
    print(row)
