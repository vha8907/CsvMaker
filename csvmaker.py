### csvmaker.py
### a program that generates random numeric values to
### user-named rows, to provide testing input material
### for other programs.

import csv, random

column_Number = 10
active_Columns = []
possibleNames = list(ascii_uppercase)
for i in range(column_Number):
    active_Columns.append(possibleNames[i])

print(active_Columns)

with open("testfile.csv", 'w', newline='') as f:
    csv_w = csv.DictWriter(f, fieldnames=['Numbers', 'MoreNumbers'])
    csv_w.writeheader()