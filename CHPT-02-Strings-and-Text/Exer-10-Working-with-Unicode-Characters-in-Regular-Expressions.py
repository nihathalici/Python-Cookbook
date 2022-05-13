# Exer-10-Working-with-Unicode-Characters-in-Regular-Expressions.py

import re

num = re.compile('\d+')
print( num.match('123') )
print(num.match('\u0661\u0662\u0663'))
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

###

pat = re.compile('stra\u00dfe', re.IGNORECASE)

s = 'straße'

print( pat.match(s) )

print( pat.match(s.upper()) )

print( s.upper() )

