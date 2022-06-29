# Exer-05-Turning-a-Dictionary-into-XML

from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(e)

###

from xml.etree.ElementTree import tostring

print(tostring(e))

###

e.set('_id', '1234')

print(tostring(e))

###

def dict_to_xml_str(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key, val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

d = { 'name' : '<spam>'}

print( dict_to_xml_str('item', d) )

# Proper XML creation
e = dict_to_xml('item', d)
print(tostring(e))

###

from xml.sax.saxutils import escape, unescape

print( escape('<spam>') )
print( unescape('<spam>') )
        
    
    
