# Exer-01-Writing-Functions-That-Accept-Any-Number-of-Arguments

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))

###

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element

# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print( make_element('item', 'Albatross', size='large', quantity=6) )

# Creates '<p>&lt;spam&gt;</p>'
print( make_element('p', '<spam>'))

###

def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict

###

def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass

