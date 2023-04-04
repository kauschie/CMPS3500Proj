"""

NAMES: Irvin Neri, Michael Kausch
ASGT: Class Project
ORGN: CSUB - CMPS 3500
FILE: ClassProjectGroup6.py
DATE: 3/30/2023

"""

# TODO:
#   - Data Structure for holding whether column vals are strings or floats
#   - this should coincide with the excel spreadsheet as well?



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
                    foo(kwargs.get('arg_list'))
                else:
                    foo()
                print(response, "is not in the range of acceptable values.")
                print("Enter a value between", min_val, "and", max_val)
        except:
            os.system('clear')
            
            if 'arg_list' in kwargs:
                foo(kwargs.get('arg_list'))
            else:
                # print('arg list not found so calling reg foo()')
                # input()
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
    # print("menu_list passed in:")
    # print(menu_list)
    # if (menu_list == None):
    #     menu_list = files.getCsvFileList()
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
        

def printDropHeaders(excl_header_list):
    printHeaders(excl_header_list)
    print("Enter a column number to drop")
    print("Enter -1 to finish entering columns")
    
def printInclHeaders(incl_header_list):
    printHeaders(incl_header_list)
    print("Enter a column number to add")
    print("Enter -1 to finish entering columns")    
   
def printHeaders(header_list):
    for i in range(len(header_list)):
        print(f"[{i}] {header_list[i]}")
    
def printDescribeColMenu(incl_header_list):
    print("Describe Columns:")
    print("*****************")
    print("*****************")
    printHeaders(incl_header_list)
    print("Enter the column number to desribe")
    print("Enter -1 to finish entering columns")    
    
def printSearchMenu(header_list):
    print("Search Element in Column:")
    print("**************************")
    for i in range(len(header_list)):
        print(f"[{i}] {header_list[i]}")   
    print("Select the column number to perform a search")
    print("Enter -1 to finish entering columns")

def printDataAnalysis(df):
    print("Data Analysis:")
    print("***************")
    print("Show the total unique count of crimes per year sorted in descending order:")
    # printTotalUniqueCount(df) # TODO
    print(f"\nShowt he top 5 areas with the most crime events in all years:")
    # printTopFiveAreas(df) # TODO
    print("Show all months and the unique total count of crimes sorted in increasing order.")
    # printMonthsUniqueCrimes(df) # TODO
    print("Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.")
    # printTop10Streets(df) # TODO
    print("Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.")
    # printTop5HWood(df) # TODO
    print("Print the details of the crime that that took the most time (in hours) to be reported.")
    # printMostTime(df) # TODO
    print("Show the 10 top most common crime types (Crm Cd Desc) overall across all years.")
    # printMostCommonCrime(df) # TODO
    print("Are woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.")
    # printLALunchTime(df) # TODO
    print("What is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.")
    # printCCFrauds(df) # TODO
    print("List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018 in West LA.")
    # printOlderManTop5(df) # TODO


def printMenu():
    print("  Print Menu  :")
    print("***************")
    print(f"\t[0] = first 100 lines")
    print(f"\t[1] = first 1000 lines")
    print(f"\t[2] = first 5000 lines\n")
    print(f"Select how many rows to print")
    print("Enter -1 to go back")


'''Main Logic // Menu loop'''
def main():
    
    menu_option = None
    data_frame = pd.DataFrame()
    error_msg = ""
    included_headers = []
    excluded_headers = []
    all_headers = []
    
    data_bools = [dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #0
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #1
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #2
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #3
                    
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #4
                    
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #5
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #6
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #7
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #8
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #9
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #10
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #11
                    
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #12
                    
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=False, max=False), #13
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=False, max=False), #14
                    
                    dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #15
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #16
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #17
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #18
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #19
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #20
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #21
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #22
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #23
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #24
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #25
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #26
                    
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #27
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #28
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True)] #29
    
    while (menu_option != 5):
        os.system("clear")
        if (error_msg != ""):
            print(error_msg)
            error_msg = ""
        
        printBaseMenu()
        menu_option = getResponse(printBaseMenu, 1, 5)
        # print("you selected option", menu_option)   #debug
        
        
        if (menu_option== 1):
            os.system("clear")
            menu_list = getCsvFileList()
            printDataSelectMenu(menu_list)
            sub_menu_option = getResponse(printDataSelectMenu, 1, len(menu_list), arg_list=menu_list)
            print("calling readFile on",menu_list[sub_menu_option-1])
            
            
            try:
                s_time = time.time()
                data_frame = readFile(menu_list[sub_menu_option-1])
                data_frame
                e_time = time.time()
                print("[start time]", s_time)
                print("[end time]", e_time)
                print("Time to load:", (e_time-s_time),"sec.")
                included_headers = list(data_frame.columns)
                all_headers = included_headers.copy() # save backup of all column names
                # print("included headers:")
                # print(included_headers)
                print(f"Total Columns Read: {len(all_headers)}")
                print(f"Total Rows Read (ndim): {len(data_frame.index)}")
                # print(f"\nTotal Elements (Not null) in each category:\n\n{data_frame.notna().sum()}")
                
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
                if (print_msg != "" ):
                    print(print_msg)
                    print_msg = ""
                printDataExpMenu()
                sub_menu_option = getResponse(printDataExpMenu, 21, 26)
                col_number = 0

                if (sub_menu_option == 21):
                    # list all columns
                    
                    print("*****************")
                    print("*****************")
                    print("Included Columns:")
                    print("*****************")
                    if (len(included_headers) > 0):
                        printHeaders(included_headers)
                    else:
                        print("No columns are currently included")
                    print("*****************")
                    print("*****************")
                    print("Excluded Columns:")
                    print("*****************")
                    if (len(excluded_headers) > 0):
                        printHeaders(excluded_headers)
                    else:
                        print("No columns are currently excluded")
                    print("*****************")
                    print("*****************")
                    input(f"\npress enter to continue...")
                    continue
                    
                elif (sub_menu_option == 22):
                    # Drop Columns
                    while (col_number != -1):
                        printDropHeaders(included_headers)
                        col_number = getResponse(printDropHeaders, -1, len(included_headers)-1, arg_list=included_headers)
                        # print("col_number now",col_number)
                        
                        if (col_number != -1):
                            excluded_headers.append(included_headers[col_number])
                            # print(f"excluded headers last: {excluded_headers[-1]}")
                            included_headers.remove(included_headers[col_number])
                            # print("included_headers now***")
                            # print(included_headers)
                            
                    print("Finished removing columns")
                    print(f"There are currently {len(excluded_headers)} items being excluded.")
                    input("press any key to continue...")
                    col_number = 0
                    
                elif (sub_menu_option == 23):
                    # Desribe Columns
                    # input("describing the columns..")
                    
                    printDescribeColMenu(included_headers)
                    col_number = getResponse(printDescribeColMenu, -1, len(included_headers)-1, arg_list=included_headers)
                    if (col_number == -1):
                        col_number = 0
                        continue
                    
                    # TODO: function to retrieve all of the stats: describeColumn
                    #  - return dictionary of count, unique, mean, median, mode, stdev, variance, minimum, maximum

                    
                    print(f"{included_headers[col_number]} stats:")
                    print("============================")

                    try:
                        s_time = time.time()
                        #stats = describeColumn(data_frame, included_headers[col_number]) # TODO
                        e_time = time.time()
                        # printStats(stats) # TODO
                        
                        print("stats printed successfully!")
                        print("Time to process is", (e_time-s_time),"sec.")
                    except:
                        print("stats did not process successfully")
                        
                    print("====== End Print ======")
                    input("Press any key to continue...")
                        
                    continue
                    
                elif (sub_menu_option == 24):
                    # Search Element in Column
                    # input("searching the columns..")
                    printSearchMenu(all_headers)
                    col_number = getResponse(printSearchMenu, -1, len(all_headers)-1, arg_list=all_headers)
                    if (col_number == -1):
                        col_number = 0
                        continue
                    
                    search_ele = input("Enter the search value: ")
                    
                    # TODO: Need to make 1:1 list of variable type so that I can 
                    #       check and see if the correct element was input

                    is_found = False
                    s_time = time.time()
                    # should return a bool
                    # is_found = search(data_frame, col_number, search_ele) # TODO: search function
                    e_time = time.time()
                    
                    
                    if (is_found):
                        print("stats printed successfully!")
                        print("Time to process is", (e_time-s_time),"sec.")
                    else:
                        print(f"could not locate (({search_ele})) in the data")
                        print("Total search time was", (e_time-s_time),"sec.")
                    
                    input("Press any key to continue")
                    continue
                    
                elif (sub_menu_option == 25):
                    # add back a dropped column
                    # input("adding back a dropped column...")
                     # Drop Columns
                     
                    if (len(excluded_headers) == 0):
                        print_msg = "There are currently 0 excluded columns so there's none to add back!"
                        continue
                     
                    while (col_number != -1):
                        printInclHeaders(excluded_headers)
                        col_number = getResponse(printInclHeaders, -1, len(excluded_headers)-1, arg_list=excluded_headers)
                        # print("col_number now",col_number)
                        
                        if (col_number != -1):
                            
                            included_headers.append(excluded_headers[col_number])
                            # print(f"included headers last: {included_headers[-1]}")
                            excluded_headers.remove(excluded_headers[col_number])
                            # print("excluded_headers now***")
                            # print(excluded_headers)
                            
                    print("Finished adding back columns")
                    print(f"There are currently {len(excluded_headers)} items still being excluded.")
                    col_number = 0
                    input("press any key to continue...")
                    
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
            
            printDataAnalysis(data_frame)
            
            input("Press any key to continue...")
            continue
        elif (menu_option == 4):
            # Print Data Set
            if (data_frame.empty):
                error_msg = """You haven't loaded any data yet! 
                Select option 1 from the main menu"""
                continue
            num_rows = [100, 1000, 5000]
            printMenu()
            sub_menu_option = getResponse(printMenu, -1, 3)
            
            print(f"printing {num_rows[sub_menu_option]} number of rows...\n")
            # printDataset(data_frame, num_rows) # TODO
            print("done printing")
            input("Press any key to continue...")
            
            # error_msg = "Print Data Section"
            continue
        
            # Prints specific rows in array:
            # print(data_frame[0:9])
            # print(data_frame.loc[0:9,"DR_NO"])
            # data_frame.to_csv('output.csv',)
            
        




if __name__ == '__main__':
    os.system('clear')
    main()
