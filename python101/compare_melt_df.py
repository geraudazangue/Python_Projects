# -*- coding: utf-8 -*-
import pandas as pd
import os
import numpy as np
from datetime import datetime
import time

start = time.time()

df1 = pd.read_csv('C:/CODE/RAW FILES/try2.csv', delimiter=",", encoding = "utf-8")
df2 = pd.read_csv('C:/CODE/RAW FILES/try3.csv', delimiter=",", encoding = "utf-8")
df1_col = df1.columns.values.tolist()
df2_col = df2.columns.values.tolist()

df1_melt = pd.melt(df1, id_vars=['ID'], value_vars=df1_col[2:], var_name='myVarname', value_name='myValname')
df2_melt = pd.melt(df2, id_vars=['ID'], value_vars=df2_col[2:], var_name='myVarname', value_name='myValname')
df3 = pd.merge(df1_melt, df2_melt, how='inner', on=['ID','myVarname'], suffixes=('_left', '_right'))
#df3 = df1_melt.merge(df2_melt, left_on=['ID','myVarname'], right_on=['ID','myVarname'], how='inner', suffixes=('_left', '_right'))
df_diff = df3.query('myValname_left != myValname_right')
print(df_diff.dropna())

End =time.time()
Execution_time = End - start
print(f'{Execution_time} secs')

#df1 = pd.read_excel('C:/CODE/RAW FILES/test1.xlsx', sheet_names='Sheet1')
#df2 = pd.read_excel('C:/CODE/RAW FILES/test2.xlsx', sheet_names='Feuil1')
#df1_melt = pd.melt(df, id_vars=[('A', 'D')], value_vars=['B','C'], var_name='myVarname', value_name='myValname')
#df2_melt = pd.melt(df, id_vars=[('A', 'D')], value_vars=['B','C'], var_name='myVarname', value_name='myValname')
#df3 = pd.merge(df1_melt, df2_melt, how='inner', on=['key1', 'key2'], validate="one_to_one")
#df3 = df1_melt.merge(df2_melt, left_on='lkey', right_on='rkey', suffixes=('_left', '_right'))
