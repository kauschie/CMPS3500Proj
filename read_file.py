"""
NAME: Irvin Neri
ASGT: Class Project
ORGN: CSUB - CMPS 3500
FILE: read_file.py
DATE: 3/30/2023
"""

import pandas as pd
import time

#Time to read and store data in an array
s_time = time.time()
csv_arr = pd.read_csv("Crime_Data_from_2017_to_2019.csv", quotechar='"', delimiter=',', skipinitialspace=True)    
e_time = time.time()

"""
If you want to access elements of csv_array or want to see the whole array use the following:

Prints the whole csv with the header at the top and row nums on the left side:
print(csv_arr)

Prints csv as an array without the header and row nums:
print(csv_arr.values)

Prints specific elements in array:
print(csv_arr.values[1,16])

Prints elements all elements on column 1 uptil row 4
print(csv_arr.values[:4,1])
"""
print("Read time: ", (e_time-s_time), "\n")
print(csv_arr)

