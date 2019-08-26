#concatenate files
path = r'C:\DRO\DCL_rawdata_files'                     # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
export_excel = concatenated_df.to_excel (r'C:\Users\Gael\Desktop\export_dataframe.xlsx', index = None, header=True)
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

#forward filling and backward filling
df.fillna(method='ffill')
df.bfill().ffill()

import pandas as pd

# Create a Pandas dataframe from some data.
data = [10, 20, 30, 40, 50, 60]
df = pd.DataFrame({'Heading': data,
                   'Longer heading that should be wrapped' : data})
out_path = r'C:\Users\Gael\Desktop\export_dataframe.xlsx'
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object. Note that we turn off
# the default header and skip one row to allow us to insert a user defined
# header.
df.to_excel(writer, sheet_name='Sheet1', startrow=1,startcol=0, header=False, index=False)
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#D7E4BC',
    'border': 1})
header_fmt = workbook.add_format({'font_name': 'Arial', 'font_size': 10, 'bold': True})
red_format = workbook.add_format({'bg_color':'red'})

worksheet.merge_range('B4:D4', 'Merged Range', header_format)
# Write the column headers with the defined format.
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

#concatenate : https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
