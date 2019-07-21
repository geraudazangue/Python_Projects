import glob
import os
import os.path
from pathlib import Path
from lxml import etree
import pandas as pd
from datetime import datetime
import logging
import time
input_file = pd.read_csv("C:/Users/Gael/Desktop/CODE/RAW FILES/input_file.txt", sep =" ",header=None)

Root = etree.Element("Root")
head = etree.SubElement(Root, 'Head')
title = etree.SubElement(head, 'title')
title.text = 'CPD_EMEA'
dc = etree.SubElement(head, 'dateCreated')
dc.text = str(datetime.today())
dm = etree.SubElement(head, 'dateModified')
dm.text = str(datetime.today())
body = etree.SubElement(Root, 'body')
range = ['Computer','Fantasy']

#USE MY TIME TO NOT ERASEN TIME MODULE
mytime = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')

file_path = "C:/Users/Gael/Desktop/CODE/RAW FILES/{0}".format('Converted_file_' + time +'.xml')
for p in  Path('C:/Users/Gael/Desktop/CODE/test').glob('**/*.xml'):
context = etree.iterparse(str(p), events=('end', ))
for event, elem in context:
#Thisnis the event launcher
    if elem.tag == 'book':
        if elem.find('genre').text in input_file.value:
            body.append(elem)
            print(XML_OUTPUT)
    if (elem.tag == 'PRODUCT') :
            if (elem.find('Civilté').text in range):
                body.append(elem)
                
XML_OUTPUT = etree.tostring(Root, pretty_print=True, encoding='UTF-8', xml_declaration=True)
with open(file_path, "wb") as writter:
    writter.write(XML_OUTPUT)

#attention point etree istead of element tree is used.
