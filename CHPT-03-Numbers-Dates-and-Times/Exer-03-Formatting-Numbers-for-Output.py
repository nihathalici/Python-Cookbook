# Exer-03-Formatting-Numbers-for-Output.py

x = 1234.56789

print( format(x, '0.2f') )

print( format(x, '>10.1f') )

print( format(x, '<10.1f') )

print( format(x, '^10.1f') )

print( format(x, ',') )

print( format(x, '0,.1f') )

print( format(x, 'e') )

print( format(x, '0.2E') )

###

print('The value is {:0,.2f}'.format(x))

###

print( format(x, '0.1f') )

print( format(-x, '0.1f') )

###

swap_separators = { ord('.'):',', ord(','):'.' }
print( format(x, ',').translate(swap_separators) )

###

print( '%0.2f' % x )

print( '%10.1f' % x )

print( '%-10.1f' % x ) 
