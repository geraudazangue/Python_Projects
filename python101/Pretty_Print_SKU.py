
import glob
import os
import os.path
from pathlib import Path
from lxml import etree
import pandas as pd


for p in  Path('C:/RTC/Scripts & Tools & Files/Python/Pretty_Print_SKU').glob('**/*.xml'):

    xml = etree.parse(str(p))
    XML_OUTPUT = etree.tostring(xml, pretty_print=True)

    with open(p, "wb") as writter:
        writter.write(XML_OUTPUT)
