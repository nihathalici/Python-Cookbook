# Exer-03-Printing-with-a-Different-Separator-or-Line-Ending
"""
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i, end=' ')
"""
print(','.join(['ACME', '50', '91.5']))

###

row =  ('ACME', 50, 91.5)
# print(','.join(row)) # TypeError

print(','.join(str(x) for x in row))

print(*row, sep=',')
