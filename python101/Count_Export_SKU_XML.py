# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:54:46 2019

@author:  Geraud AZANGUE
"""

#from xml.etree import ElementTree as ET

from lxml import etree
import pandas as pd

value = []

xml = etree.parse("C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/CPDEMEA_CPDHUBRU-KZ_20190522_165904.001-004.xml")
count = len(xml.findall(".//*[A0001]"))
print(count)

for nb in xml.findall('.//PRODUCT'):
    s_sku = nb.find("A0001").text
    value.append(s_sku)

d = {'SKU':value}
df = pd.DataFrame(d)
export_excel = df.to_excel (r'C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/export_NB_SKU.xlsx', index = None, header=True)
