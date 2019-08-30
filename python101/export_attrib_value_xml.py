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
Attribute_to_extract = ['A0001','A0186','A0070','A1257','A0157']

def parser_xml(tags, path):
    tree = etree.iterparse(str(path))  
    for event, node in tree: 
        if node.tag in tags:
            yield [node.tag, node.text]
			
#solution 1:
list_of_generator = [parser_xml(Attribute_to_extract,file) for file in Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml')
															if file.is_file()]
for generator in list_of_generator:
    for  attribute_value in generator:
		list_of_attribute_value.append(attribute_value)
		
 #solution 2:     
list_of_attribute_value2 = list(chain.from_iterable(parser_xml(Attribute_to_extract,file) for file in Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml')))
 
df_attributes_value = pd.DataFrame(list_of_attribute_value, columns=['Attribute','Value'])
#Nasty, yes I know
df_prefinal_attribute_extract = df_attributes_value.pivot(columns='Attribute', values='Value').bfill().ffill()
df_flat_extract = df_prefinal_attribute_extract.drop_duplicates()
#export_excel = df.to_excel (r"C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/{0}".format('EXPORT_ELIX2SAP' + datestring + '.xlsx'), index = None, header=True)
End =time.time()
Execution_time = End - start
print(f'{Execution_time} secs')