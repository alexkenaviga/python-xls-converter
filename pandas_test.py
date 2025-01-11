import pandas as pd
import time
import sys

file_path = sys.argv[1]
sheet_name = sys.argv[2]

start = time.time()
pd.read_excel(file_path, header=[0])
end = time.time()
print(f"FILE\t\tfinished in {round(end - start, 2)}")

start = time.time()
pd.read_excel(file_path, sheet_name=sheet_name, header=[0])
end = time.time()
print(f"SHEET\t\tfinished in {round(end - start, 2)}")

start = time.time()
with pd.ExcelFile(file_path) as xls:
    end = time.time()
    print(f"EF\t\tfinished in {round(end - start, 2)}")

    start = time.time()
    pd.read_excel(xls, sheet_name)
    end = time.time()
    print(f"EF SHEET\tfinished in {round(end - start, 2)}")
