"""

NAMES: Irvin Neri, Michael Kausch
ASGT: Class Project
ORGN: CSUB - CMPS 3500
FILE: ClassProjectGroup6.py
DATE: 3/30/2023


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

def getResponse(foo, max_val, min_val=1):
    '''Takes in a print function (foo) and tests against minumum
        and maximum menu options.
        Function returns an integer value that met the response criteria'''
    response = -1
    
    while ((response < min_val) or (response > max_val)):
        # foo()
        
        try:
            str_response = input("Enter your choice: ")
            response = int(str_response)
            
            if ((response < min_val) or (response > max_val)):
                os.system('clear')
                foo()
                print(response, "is not in the range of acceptable values.")
                print("Enter a value between", min_val, "and", max_val)
        except:
            os.system('clear')
            foo()
            print(str_response, "is not a valid response. Please enter an integer.")
            response = -1
        
    return response
            
def printBaseMenu():
    print("Main Menu:")
    print("**********")
    print("1. Load Data")
    print("2. Explore Data")
    print("3. Data Analysis")
    print("4. Print Data Set")
    print("5. Quit")

def printDataSelectMenu(menu_list=None):
    """prints data select menu

    Args:
        menu_list (list of menu items, optional): Defaults to None.
    """
    
    if (menu_list == None):
        menu_list = files.getCsvFileList()
    print("Load data set:")
    print("***************")
    
    print(f"Please select from the following available files:")
    for i in range(len(menu_list)):
        print(f"\t[{i+1}]: {menu_list[i]}")
    
def main():
    printBaseMenu()
    menu_option = getResponse(printBaseMenu, 5, 1)
    print("you selected option", menu_option)   #debug
    if (menu_option == 1):
        menu_list = getCsvFileList()
        printDataSelectMenu(menu_list)
        sub_menu_option = getResponse(printDataSelectMenu, len(menu_list), 1)
        print("calling readFile on",menu_list[sub_menu_option-1])
        


if __name__ == '__main__':
    os.system('clear')
    main()
