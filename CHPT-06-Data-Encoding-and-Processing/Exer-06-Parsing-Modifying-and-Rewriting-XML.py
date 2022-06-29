# Exer-06-Parsing-Modifying-and-Rewriting-XML

from xml.etree.ElementTree import parse, Element

doc = parse('pred.xml')

root = doc.getroot()

print(root)

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
print( root.getchildren().index(root.find('nm')) )

e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# Write back to a file
doc.write('newpred.xml', xml_declaration=True)



