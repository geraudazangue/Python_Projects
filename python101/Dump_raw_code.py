############### XML MANIPULATION #################
Write to to a file XML
tree = ET.ElementTree(Root)
tree.write('C:/Users/Gael/Desktop/CODE/RAW FILES/filename.xml', pretty_print=True, xml_declaration=True)
Using xpath instead of findall
for nb in xml.xpath("/users/user/nom"):
    print(nb.text)
    value.append(nb.text)

Open and read a file
f = open('C:/Users/Gael/Desktop/CODE/python/COUNT SKU PY/testbook.xml')
test= f.read()
Load in json type a file
json.loads(jsonfile.json)

Rename a file
os.rename("C:/Users/Gael/Desktop/CODE/RAW FILES/Converted_file", file_path)

Accessing a Dir or file
path = r'C:\DRO\DCL_rawdata_files'                     # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

a= glob.glob('C:/Users/Gael/Desktop/TESTDOSSIER/*.xml')
a = os.listdir('C:/Users/Gael/Desktop/CODE/vba')
b = os.path.realpath('a')
p= list(Path('C:/Users/Gael/Desktop/TESTDOSSIER').glob('**/*.xml'))


##########  PANDA ##################
df = df[df['A'].isin(list)]
df5 = df4.dropna(how='all')
df5 = df4.FILLna(0)"

#forward filling and backward filling
df.fillna(method='ffill')
df.bfill().ffill()

delete all rows for which column 'Age' has value greater than 30 and Country is India
indexNames = df[ (df['Age'] >= 30) & (df['Country'] == 'India') ].index
df.drop(indexNames , inplace=True)

Group by transform to avoid groupby + merge
df.groupby('ID')["group_value"].transform('sum or max,..')

Removing data with different column value
df = df[df['S'] != df['T']]
df = df.query("S != T")

Use conditions to remove columns with numpy
np.where

#SQL QUERY WITH INPUT FILE
with open('file', 'r') as file:
	list = [line.strip('\n') for line in file]

list_id = ','.join(["'%s'" %id for id in list])
sql_query = '''SELECT *
				FROM TABLE
				WHERE ID in ({})
			'''.format(list_id)
df = pd.read_sql(sql_query, cnxn, params=(*list))

#SPLIT LARGE FILES
for i, chunk in enumerate(pd.read_csv('Extract', chunksize=100000)):
	chunk.to_csv('Extract{}.csv'.format(i), index='False')
size = 10000
list_of_df = [df.iloc[i:i + size -1,:] for i in range(0,len(df),size)]

#MERGE MANY FILES
from glob import iglob
path = r'C:\user\your\path\**\*.csv'
df = pd.concat((pd.read_csv(f) for f in iglob(path, recursive=True)), ignore_index=True)

############## FOOD FOR THOUGHT ON ODBC CONNEXION#################
 Using a DSN, but providing a password as well
cnxn = pyodbc.connect('DSN=test;PWD=password')
 Create a cursor from the connection
cursor = cnxn.cursor()
cursor.execute("select user_id, user_name from users")
row = cursor.fetchone()
row = cursor.fetchall()

cursor.execute("""
    select user_id, user_name
      from users
     where last_logon < ?
       and bill_overdue = ?
""", [datetime.date(2001, 1, 1), 'y'])

####INSTALL MODULE#####
import subprocess
import sys

try:
    import xs
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", '-r', 'pydev_requirements.txt'])