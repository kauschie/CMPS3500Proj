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


def getPrintColumns(dframe):
    headers = list(dframe.columns)
    print(headers)

#Time to read and store data in an array

def readFile(file_name="Crime_Data_from_2017_to_2019.csv"):
    s_time = time.time()
    csv_arr = pd.read_csv(file_name, quotechar='"', delimiter=',', skipinitialspace=True)    
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
    # print(csv_arr)

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

def getResponse(foo, min_val, max_val, **kwargs):
    '''Takes in a print function (foo) and tests against minumum
        and maximum menu options.
        Function returns an integer value that met the response criteria'''
    response = -2
    
    if 'arg_list' not in kwargs:
        pass
    
    # if 'arg_list' in kwargs:
    #     print(f"you passed in an arg_list:")
    #     print(f"{kwargs.get('arg_list')}")
    
    while ((response < min_val) or (response > max_val)):
        # foo()
        
        try:
            str_response = input("Enter your choice: ")
            response = int(str_response)
            
            if ((response < min_val) or (response > max_val)):
                os.system('clear')
                if 'arg_list' in kwargs:
                    foo(arg_list)
                else:
                    print('arg list not found so calling reg foo()')
                    input()
                    foo()
                print(response, "is not in the range of acceptable values.")
                print("Enter a value between", min_val, "and", max_val)
        except:
            os.system('clear')
            foo()
            print(str_response, "is not a valid response. Please enter an integer.")
            response = -2
        
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
        
        
def printDataExpMenu():
    print("Exploring Data:")
    print("**********")
    print("21. List all Columns:")
    print("22. Drop Columns:")
    print("23. Describe Columns:")
    print("24. Search Element in Column:")
    print("25. Add Back a Dropped Column:")
    print("26. Back to the Main Menu")
        

def printHeaders(headerList):
    for i in range(len(headerList)):
        print(f"[{i}] {headerList[i]}")
    
def main():
    
    menu_option = None
    data_frame = pd.DataFrame()
    error_msg = ""
    included_headers = []
    excluded_headers = []
    
    
    while (menu_option != 5):
        os.system("clear")
        if (error_msg != ""):
            print(error_msg)
            error_msg = ""
        
        printBaseMenu()
        menu_option = getResponse(printBaseMenu, 1, 5)
        print("you selected option", menu_option)   #debug
        
        if (menu_option== 1):
            menu_list = getCsvFileList()
            printDataSelectMenu(menu_list)
            sub_menu_option = getResponse(printDataSelectMenu, 1, len(menu_list))
            print("calling readFile on",menu_list[sub_menu_option-1])
            
            
            try:
                s_time = time.time()
                data_frame = readFile(menu_list[sub_menu_option-1])
                e_time = time.time()
                print("[start time]", s_time)
                print("[end time]", e_time)
                print("Time to load:", (e_time-s_time),"sec.")
                included_headers = list(data_frame.columns)
                # print("included headers:")
                # print(included_headers)
            except:
                error_msg = f"could not load data file {menu_list[sub_menu_option-1]}"

            input("press enter to continue...")
            continue
            
        elif (menu_option == 2):
            # Explore Data
            os.system("clear")
            if (data_frame.empty):
                error_msg = """You haven't loaded any data yet!
                Select option 1 from the main menu"""
                continue
            
            # print("Data Exploration Section")
            sub_menu_option = 0
            print_msg = ""
            while (sub_menu_option != 26):
                # get user input until correct
                os.system("clear")
                printDataExpMenu()
                sub_menu_option = getResponse(printDataExpMenu, 21, 26)
                col_number = 0

                if (print_msg != "" ):
                    print(print_msg)
                    print_msg = ""
                
                if (sub_menu_option == 21):
                    # list all columns
                    
                    print("Included Headers:")
                    print("*****************")
                    printHeaders(included_headers)
                    print("*****************")
                    print("Excluded Headers:")
                    print("*****************")
                    printHeaders(excluded_headers)
                    input("press enter to continue...")
                    continue
                    
                elif (sub_menu_option == 22):
                    # Drop Columns
                    while (col_number != -1):
                        printHeaders(included_headers)
                        print("Enter a column number to drop")
                        print("Enter -1 to finish entering columns")
                        col_number = getResponse(printHeaders, -1, len(included_headers)-1, arg_list=included_headers)
                        print("col_number now",col_number)
                        
                        
                        if (col_number != -1):
                            excluded_headers.append(included_headers[col_number])
                            print(f"excluded headers last: {excluded_headers[-1]}")
                            included_headers.remove(included_headers[col_number])
                            print("included_headers now***")
                            print(included_headers)
                            
                    print("Finished removing columns")
                    input("press any key to continue...")
                    
                elif (sub_menu_option == 23):
                    # Desribe Columns
                    input("describing the columns..")
                    
                elif (sub_menu_option == 24):
                    # Search Element in Column
                    input("searching the columns..")
                    
                elif (sub_menu_option == 25):
                    # add back a dropped column
                    input("adding back a dropped column...")
                    
                elif (sub_menu_option == 26):
                    # back to the main menu
                    input("Back to the main menu...")
                    
            
            
            
            
            error_msg = "Data Exploration Section"
            continue
            
        elif (menu_option == 3):
            # Data Analysis
            if (data_frame.empty):
                error_msg = """You haven't loaded any data yet! 
                Select option 1 from the main menu"""
                continue
            
            print("Data Analysis Section")
            error_msg = "Data Analysis Section"
            continue
        elif (menu_option == 4):
            # Print Data Set
            if (data_frame.empty):
                error_msg = """You haven't loaded any data yet! 
                Select option 1 from the main menu"""
                continue
                
            print("Print Data Section")
            error_msg = "Print Data Section"
            continue
            # getPrintColumns(data_frame)
            
            
            # Prints specific rows in array:
            # print(data_frame[0:9])
            # print(data_frame.loc[0:9,"DR_NO"])
            # data_frame.to_csv('output.csv',)
            
        


if __name__ == '__main__':
    os.system('clear')
    main()
