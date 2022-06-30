# Exer-07-Parsing-XML-Documents-with-Namespaces


<?xml version="1.0" encoding="utf-8"?>
<top>
<author>David Beazley</author>
<content>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Hello World</title>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
</content>
</top>

doc.findtext('author')
doc.find('content')
doc.find('content/html')

doc.find('content/{http://www.w3.org/1999/xhtml}html')
doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title')

doc.find('content/{http://www.w3.org/1999/xhtml}html/'
         '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title')


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)

ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
doc.find(ns('content/{html}html'))
doc.findtext(ns('content/{html}html/{html}head/{html}title'))

###

from xml.etree.ElementTree import iterparse

for evt, elem in iterparse('ns2.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
