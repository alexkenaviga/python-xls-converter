import asyncio
import pandas as pd
import datetime
import sys
import os


async def convert_sheet(xls, sheet_name, query, out_dir):
	success = True
	try:
		start = datetime.datetime.now()
		print(f"[{sheet_name}] Reading sheet: {sheet_name}")
		df = pd.read_excel(xls, sheet_name=sheet_name, header=[0])

		if query is not None:
			print(f"[{sheet_name}] Filtering by: {query}")
			filtered = df.query(query)
		else:
			filtered = df

		print(f"[{sheet_name}] Writing '{out_dir}/{sheet_name}.csv'")
		filtered.to_csv(f"{out_dir}/{sheet_name}.csv", index=False)

		end = datetime.datetime.now()
		print(f"[{sheet_name}] Done in {round((end - start).total_seconds() * 1000)}ms")

	except Exception as e:  # works on python 3.x
		print(f'[{sheet_name}] Failed to convert:', repr(e))
		success = False

	return f"[{"SUCCESS" if success else "FAILED"}]\t{out_dir}/{sheet_name}.csv"


async def convert(path_to_xls, query, out_dir):
	print (f"Invoked conversion wit query '{query}' on '{path_to_xls}'")

	if os.path.isfile(path_to_xls):

		# Create output dir
		if out_dir is None:
			out_dir = f"output/{os.path.splitext(os.path.basename(path_to_xls))[0]}"
		print(f"Output destination: {out_dir}")

		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
			print(f"Directory '{out_dir}' created successfully!")

		start = datetime.datetime.now()
		# Create an ExcelFile object
		with pd.ExcelFile(path_to_xls) as xls:
			end = datetime.datetime.now()
			print(f"File leaded in {round((end - start).total_seconds() * 1000)}ms")

			# Retrieve the sheet names
			sheet_names = [s for s in xls.sheet_names if "SQL" not in s]
			print(f"Sheet names = {sheet_names}")

			print(f"Conversion Starting...")
			start = datetime.datetime.now()
			tasks = [convert_sheet(xls, sheet, query, out_dir) for sheet in sheet_names]
			results = await asyncio.gather(*tasks)
			end = datetime.datetime.now()

			print(f"Conversion completed in {round((end - start).total_seconds() * 1000)}ms")
			for result in results:
				print(f"- {result}")

	else:
		print(f"The path {path_to_xls} is not a file.")


if __name__ == '__main__':
	# python convert.py '/Users/allongo/Downloads/Forecast_AIDA/forecast.gestione_msd.xls'
	# 	"DATA_ORA_RIF>='2024-12-17' and DATA_ORA_RIF<'2024-12-18' and ID_SESSIONE=18" 'gestione_msd_20241217'

	path_to_xls_arg = sys.argv[1]
	query_arg = sys.argv[2] if len(sys.argv) > 0 and len(sys.argv[2]) != 0 else None
	out_dir_arg = sys.argv[3] if len(sys.argv) > 3 else None

	asyncio.run(convert(path_to_xls_arg, query_arg, out_dir_arg))
