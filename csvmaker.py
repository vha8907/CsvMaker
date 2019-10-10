### csvmaker.py
### a program that generates random numeric values to
### user-named rows, to provide testing input material
### for other programs.

import csv, random
from string import ascii_uppercase as uppercase

def makeCSV(col_N, row_N, range_Start, range_End):

    # generator of columns (using the alphabet in uppercase as name reference)
    columns = col_N
    column_Reference = list(uppercase)
    column_Names = []
    for n in range(columns):
        column_Names.append(column_Reference[n])

    # generates random numeric content to fill in the rows
    rows = row_N
    row_Data = []
    for n in range(rows):
        row_Data.append([random.randint(range_Start, range_End) for x in range(columns)])

    # creates a csv file in the present working directory:
    with open("testfile.csv", 'w') as f:
        csv_w = csv.writer(f)
        csv_w.writerow(column_Names)
        for r in row_Data:
            csv_w.writerow(r)