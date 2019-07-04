import xml.etree.ElementTree as ET
import os

context = ET.iterparse('C:/Users/Gael/Desktop/CODE/python/COUNT SKU PY/test.xml', events=('end', ))
for event, elem in context:
if elem.tag == 'row':
    title = elem.find('NAME').text
    filename = format(title + ".xml")
    with open(filename, 'wb') as f:
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        f.write("<root>\n")
        f.write(ET.tostring(elem))
        f.write("</root>")


range = ['Zorro','Hulk']
context = ET.iterparse('C:/Users/Gael/Desktop/CODE/python/COUNT SKU PY/test.xml', events=('end', ))
for event, elem in context:
    if elem.tag == 'user':
        if elem.find('nom').text in range:
            title = elem.find('metier').text
            print(title)
            XML_OUTPUT = etree.tostring(elem, pretty_print=True)
            print(XML_OUTPUT)
#attention point etree istead of element tree is used.


context = ET.iterparse('file.xml', events=('end', ))
index = 0
for event, elem in context:
    if elem.tag == 'row':
        index += 1
        filename = format(str(index) + ".xml")
        with open(filename, 'wb') as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(ET.tostring(elem))
