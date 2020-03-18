import glob
import os
import os.path
from pathlib import Path
from lxml import etree
import pandas as pd
from datetime import datetime
import time
#never ever do this
from itertools import *

start = time.time()
datestring = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
list_of_attribute_value = []
Attribute_to_extract = ['first','second','third','last_tag']

for path in Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml'):
    tree = etree.iterparse(str(path))
    for event, node in tree:
            if node.tag == 'first':
                sku = node.text
                t = 0
                myocc = ''.join([sku,'-',str(t)])
                newmyocc = ''.join([sku,'-',str(t)])
            if node.tag == Attribute_to_extract[-1]:
                t = t + 1
                newmyocc = ''.join([sku,'-',str(t)])
            if node.tag in Attribute_to_extract:
                list_of_attribute_value.append([myocc, node.tag, node.text])
                myocc = newmyocc
#solution 2: much slower
def parser_xml(tags, path):
    tree = etree.iterparse(str(path))
    for event, node in tree:
        if node.tag == 'A0001':
            sku = node.text
            t = 0
            myocc = ''.join([sku,'-',str(t)])
            newmyocc = ''.join([sku,'-',str(t)])
        if node.tag == Attribute_to_extract[-1]:
            t = t + 1
            newmyocc = ''.join([sku,'-',str(t)])
        if node.tag in tags:
            yield [myocc, node.tag, node.text]
            myocc = newmyocc

list_of_attribute_value2 = list(chain.from_iterable(parser_xml(Attribute_to_extract,file)
                                for file in Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml')))
#print(list_of_attribute_value2)
df_attributes_value = pd.DataFrame(list_of_attribute_value2, columns=['myocc','Attribute','Value'])
#print(df_attributes_value)
#Nasty, yes I know
df_prefinal_attribute_extract = df_attributes_value.pivot(index="myocc", columns='Attribute', values='Value')
print(df_prefinal_attribute_extract)
export_path = r'C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/'
export_excel = df_prefinal_attribute_extract.to_excel (f'{export_path}EXPORT_{datestring}.xlsx', index = None, header=True)
End = time.time()
Execution_time = End - start
print(f'{Execution_time} secs')
