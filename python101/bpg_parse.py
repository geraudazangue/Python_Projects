import pandas as pd

#using cp437 for encoding instead of utf8
#dtype={'col1': Str, 'col2': int64}

with open("C:/Users/Gael/Desktop/CODE/RAW FILES/pipe dataset/result_contacts.txt", 'r', encoding='cp437') as f:
    # get No of columns in each line
    col_count = [ len(l.split("|")) for l in f.readlines() ]

column_names = [i for i in range(0, max(col_count))]

### Read csv
df = pd.read_csv("C:/Users/Gael/Desktop/CODE/RAW FILES/pipe dataset/result_contacts.txt", header=None, delimiter="|", names=column_names, encoding = "utf-8")
print(df.head())
