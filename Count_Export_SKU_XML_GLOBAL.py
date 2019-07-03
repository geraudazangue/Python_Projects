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

count2=0
value = []

for p in  Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml'):
    if p.is_file():
        xml = etree.parse(str(p))
        count = len(xml.findall(".//*[A0001]"))
        print(count)

        for nb in xml.findall('.//PRODUCT'):
            s_sku = nb.find("A0001").text
            value.append(s_sku)

    count2 = count + count2

print(count2)

d = {'SKU':value}
df = pd.DataFrame(d)
datestring = datetime.strftime(datetime.now(), ' %Y%m%d_%H%M%S')
export_excel = df.to_excel (r"C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/{0}".format('export_NB_SKU' + datestring + '.xlsx'), index = None, header=True)

#a= glob.glob('C:/Users/Gael/Desktop/TESTDOSSIER/*.xml')
#a = os.listdir('C:/Users/Gael/Desktop/CODE/vba')
#b = os.path.realpath('a')
#p= list(Path('C:/Users/Gael/Desktop/TESTDOSSIER').glob('**/*.xml'))

        #for nb in xml.xpath("/users/user/nom"):
            #print(nb.text)
            #value.append(nb.text)
#export_excel = df.to_excel (r'C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/export_dataframe.xlsx', index = None, header=True)
