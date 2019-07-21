#Write to to a file XML
#tree = ET.ElementTree(Root)
#tree.write('C:/Users/Gael/Desktop/CODE/RAW FILES/filename.xml', pretty_print=True, xml_declaration=True)

#Open and read a file
#f = open('C:/Users/Gael/Desktop/CODE/python/COUNT SKU PY/testbook.xml')
#test= f.read()
#Load in json type a file
#json.loads(jsonfile.json)

#Rename a file
#os.rename("C:/Users/Gael/Desktop/CODE/RAW FILES/Converted_file", file_path)

#Accessing a Dir or file
#a= glob.glob('C:/Users/Gael/Desktop/TESTDOSSIER/*.xml')
#a = os.listdir('C:/Users/Gael/Desktop/CODE/vba')
#b = os.path.realpath('a')
#p= list(Path('C:/Users/Gael/Desktop/TESTDOSSIER').glob('**/*.xml'))

#Using xpath instead of findall
#for nb in xml.xpath("/users/user/nom"):
    #print(nb.text)
    #value.append(nb.text)


##########PANDA ######"
#df5 = df4.dropna(how='all')
#df5 = df4.FILLna(0)"

# delete all rows for which column 'Age' has value greater than 30 and Country is India
#indexNames = df[ (df['Age'] >= 30) & (df['Country'] == 'India') ].index
#df.drop(indexNames , inplace=True)

#Group by transform to avoid groupby + merge
#df.groupby('ID')["group_value"].transform('sum or max,..')

#df = df[df['S'] != df['T']]
#df = df.query("S != T")
