# -*- coding: utf-8 -*-
import pandas as pd
from lxml import etree
import xml.etree.cElementTree as ET
from datetime import datetime
import os

df = pd.read_excel('C:/Users/Gael/Desktop/CODE/RAW FILES/test.xlsx', sheet_names='test1')
tags= df.columns.values

Root = etree.Element("Root")

head = etree.SubElement(Root, 'Head')
title = etree.SubElement(head, 'title')
title.text = 'CPD_EMEA'
dc = etree.SubElement(head, 'dateCreated')
dc.text = str(datetime.today())
dm = etree.SubElement(head, 'dateModified')
dm.text = str(datetime.today())

time = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')

file_path = "C:/Users/Gael/Desktop/CODE/RAW FILES/{0}".format('Converted_file_' + time +'.xml')
body = etree.SubElement(Root, 'body')
for rowOfCellObjects in df.values:
    PRODUCT = etree.SubElement(body, 'PRODUCT')
    j=0

    for cellObj in rowOfCellObjects:
        if str(cellObj) == "nan":
            j = j+1
            continue

        nom = etree.SubElement(PRODUCT, tags[j])
        nom.text = str(cellObj)
        j= j+1

print(etree.tostring(Root, pretty_print=True))
XML_OUTPUT = etree.tostring(Root, pretty_print=True, encoding='UTF-8', xml_declaration=True)
#tree = ET.ElementTree(Root)
#tree.write('C:/Users/Gael/Desktop/CODE/RAW FILES/filename.xml', pretty_print=True, xml_declaration=True)

with open(file_path, "wb") as writter:
    writter.write(XML_OUTPUT)

#os.rename("C:/Users/Gael/Desktop/CODE/RAW FILES/Converted_file", file_path)
