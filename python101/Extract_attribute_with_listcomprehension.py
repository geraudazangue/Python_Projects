import glob
import os
import os.path
from pathlib import Path
from lxml import etree
import pandas as pd
from datetime import datetime
import time

start_time = time.time()
value2 = []
timestamp = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')

test_list = [etree.parse(str(p)) for p in Path('C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY').glob('**/*.xml')
                                 if p.is_file()]

def find_sku(xml):
    list_find_all_sku = [sku_tree for sku_tree in xml.findall('.//PRODUCT')]
    sku_value_list = [sku.find("A0001").text for sku in list_find_all_sku]
    return(sku_value_list)

for total in test_list:
    value2.extend(sku_find(total))
print(len(value2))

d = {'SKU_EXPORT_SAP':value2}
df = pd.DataFrame(d)
#export_excel = df.to_excel (r"C:/RTC/Scripts & Tools & Files/Python/COUNT SKU PY/{0}".format('EXPORT_ELIX2SAP' + timestamp + '.xlsx'), index = None, header=True)
End_time =time.time()
Execution_time = End_time - start_time
print(f"{Execution_time},secs")
