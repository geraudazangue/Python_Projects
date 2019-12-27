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


######FILLING EXCEL FILE ########
from openpyxl import load_workbook
import glob
import os

directory = r'C:\Users\Gael\Desktop\CODE\python'
all_files = glob.glob(os.path.join(directory, "*.xlsx))

def forwardfill(file):
	df_flat_file = pd.read_excel(file, sheet_names=1, skiprows=1)
	df_filled_file = df_flat_file.ffill()
	book = load_workbook(file)
	writer = pd.ExcelWriter(file, engine='openpyxl')
	writer.book = book
	writer.sheets = book.worksheets
	writer.sheets = {ws.title: ws for ws in book.worksheets}
	
	for sheetname in writer.sheets:
		df_filled_file.to_excel(writer, sheet_name=sheetname, startrow=1, startcol=0, index=False, header=False)
	writer.save()

for path in all_files:
	forwardfill(path)
