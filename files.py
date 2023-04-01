"""

NAMES: Irvin Neri, Michael Kausch
ASGT: Class Project
ORGN: CSUB - CMPS 3500
FILE: files.py
DATE: 3/30/2023


Modifications:
    Date: 4/1/23

        - encapsulated code into function call
        - added more relevant function calls for files / file reading
"""


import pandas as pd
import time
import os

#Time to read and store data in an array

def readFile(file_name):
    s_time = time.time()
    csv_arr = pd.read_csv(file_name="Crime_Data_from_2017_to_2019.csv", quotechar='"', delimiter=',', skipinitialspace=True)    
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

    Note: all null data points are set to NaN by default
    """
    print("Read time: ", (e_time-s_time), "\n")
    print(csv_arr)

    return(csv_arr)


'''Gets a list of csv files in the current working directory'''
def getCsvFileList():
    os.chdir(os.getcwd())   # change directory to current working directory
    files = []  # make an empty list
    for file in os.listdir():   #iterate through all filenames in ls
        # previous method:
        # file_lower = file.lower()
        # print(file_lower)
        # dot_pos = file.find('.')    # find where the . is for the file extension
        # ext = file[dot_pos+1:]  # get a string of what's leftover from the . onward
        # if (ext.lower() == "csv"):
        #     files.append(file)  # append if it's a csv file
        # easier and simpler
        
        # if ".csv" in file.lower():
        #     files.append(file)
        
        # third method: safest in case of poor file naming by professor
        ext = os.path.splitext(file)
        if (ext[1].lower() == ".csv"):
            files.append(file)    
        
    # print(files) # debug
    return files