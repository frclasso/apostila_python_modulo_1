#!/usr/bin/env python3

import pandas as pd

# Assign spreadsheet filename: file
file = '../extras3_excel_files/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Parse the first sheet and rename the columns: df1
# df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])
df1 = xl.parse(0, skiprows=[0], names=['War(country)', '2004'])

# Print the head of the DataFrame df1
print(df1.head())
print()
# Parse the first column of the second sheet and rename the column: df2
#df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country', 'AAM due to War (2002)'])
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['War, age-adjusted mortality due to', '2002'])

# Print the head of the DataFrame df2
print(df2.head())
    