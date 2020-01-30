from pandas.io.json import json_normalize
import xmltodict
import json
from datetime import datetime
from lxml import etree

#to normalise JSON to pandas dataframe
#json_normalize(data)
#https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas

xml = etree.parse('C:/Users/Gael/Desktop/CODE/python/COUNT SKU PY/testbook.xml')
XML_OUTPUT = etree.tostring(xml, pretty_print=True, encoding='UTF-8')
mytime = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
file_path = f'C:/Users/Gael/Desktop/CODE/RAW FILES/Converted_file_{mytime}.json'

print(XML_OUTPUT)
jsonString = json.dumps(xmltodict.parse(XML_OUTPUT),indent=4)

with open(file_path, 'w') as f:
    f.write(jsonString)

def removetag(tag,input_dir,target_dir):
    mytime = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
    file_path = f'{target_dir}/Converted_file_{mytime}.xml'

    for p in  Path(input_dir).glob('**/*.xml'):
    context = etree.parse(str(p))
    for nb in context.findall(".//"+x):
        nb.getparent().remove(nb)

        XML_OUTPUT = etree.tostring(context, pretty_print=True, encoding='UTF-8', xml_declaration=True)
        with open(file_path, "wb") as writter:
            writter.write(XML_OUTPUT)
