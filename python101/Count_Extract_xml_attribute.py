# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:47:15 2019

@author: Geraud AZANGUE
"""
import glob
import os
import os.path
from pathlib import Path
from lxml import etree
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
count2=0
value = []

try:
    #######Solution 1###############
    for p in  Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml'):
        if p.is_file():
            xml = etree.parse(str(p))
            count = len(xml.findall(".//*[A0001]"))
            print(count)
            for nb in xml.findall('.//PRODUCT'):
                s_sku = nb.find("A0001").text
                value.append(s_sku)
        count2 = count + count2
        logging.info('%s Nb sku', count2)
    print(count2)
 #######SOLUTION 2###############  
test_list = [etree.parse(str(p)) for p in Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml')
                                 if p.is_file()]
def find_sku(xml):
    list_find_all_sku = [sku_tree for sku_tree in xml.findall('.//PRODUCT')]
    sku_value_list = [sku.find("A0001").text for sku in list_find_all_sku]
    return(sku_value_list)

for total in test_list:
    value2.extend(sku_find(total))
print(len(value2))

d = {'SKU':value}
df = pd.DataFrame(d)
datestring = datetime.strftime(datetime.now(), ' %Y%m%d_%H%M%S')
export_excel = df.to_excel (r"C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/{0}".format('export_NB_SKU' + datestring + '.xlsx'), index = None, header=True)

except Exception as e:
  logging.exception("Exception occurred")
