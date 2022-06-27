# Exer-03-Parsing-Simple-XML-Data

from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)


for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()

print(doc)
e = doc.find('channel/title')
print(e)
print(e.tag)
print(e.text)

import lxml
