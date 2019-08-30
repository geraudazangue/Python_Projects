import pandas as pd
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
