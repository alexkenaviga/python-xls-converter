import xlrd
import pandas as pd
import datetime
import sys
import os


class Converter:

	@staticmethod
	def convert(path_to_xls, query, out_dir):
		if os.path.isfile(path_to_xls):

			# Create output dir
			if out_dir is None:
				out_dir = f"output/{os.path.splitext(os.path.basename(path_to_xls))[0]}"

			if not os.path.exists(out_dir):
				os.makedirs(out_dir)
				print(f"Directory '{out_dir}' created successfully!")

			# Create an ExcelFile object
			xls = xlrd.open_workbook(path_to_xls, on_demand=True)

			# Retrieve the sheet names
			sheet_names = xls.sheet_names()

			# Print the sheet names
			print(f"sheet_names = {sheet_names}")

			for sheet in sheet_names:
				if "SQL" not in sheet:
					start = datetime.datetime.now()
					print("-")
					print(f"Reading sheet: {sheet} of {path_to_xls}")
					df = pd.read_excel(path_to_xls, sheet_name=sheet, header=[0])
					# print(df.dtypes)

					if query is not None:
						print(f"... Filtering by: '{query}'")
						filtered = df.query(query)
					else:
						filtered = df
					
					print(f"... Writing '{out_dir}/{sheet}.csv'")
					filtered.to_csv(f"{out_dir}/{sheet}.csv", index=False)
					
					end = datetime.datetime.now()
					print(f"Done in {round((end - start).total_seconds() * 1000)}ms")

		else:
			print(f"The path {path_to_xls} is not a file.")


if __name__ == '__main__':
	# python convert.py '/Users/allongo/Downloads/Forecast_AIDA/forecast.gestione_msd.xls'
	# 	"DATA_ORA_RIF>='2024-12-17' and DATA_ORA_RIF<'2024-12-18' and ID_SESSIONE=18" 'gestione_msd_20241217'

	# print(sys.argv)

	path_to_xls_arg = sys.argv[1]
	query_arg = sys.argv[2] if len(sys.argv) > 2 else None
	out_dir_arg = sys.argv[3] if len(sys.argv) > 3 else None

	Converter.convert(path_to_xls_arg, query_arg, out_dir_arg)
