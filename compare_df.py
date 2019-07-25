import pandas as pd
import numpy as np

df1 = pd.read_excel('C:/Users/Gael/Desktop/CODE/RAW FILES/test1.xlsx', sheet_names='test1')
df2 = pd.read_excel('C:/Users/Gael/Desktop/CODE/RAW FILES/test2.xlsx', sheet_names='test2')
df_all = pd.concat([df1,df2], axis='columns',keys=['before', 'After']).drop_duplicates()
df_last = df_all.swaplevel(axis='columns')[df1.columns[1:]]
#df_last
df4 = df1.where(df1!=df2)
df4.dropna
print(df4)
def highlight_diff(data, color='yellow'):
    attr = 'background-color: {}'.format(color)
    other = data.xs('before', axis='columns', level=-1)
    return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''), index=data.index, columns=data.columns)

df_last.style.apply(highlight_diff, axis=None)
#it worked
