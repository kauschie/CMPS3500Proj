#!/usr/bin/env python3
"""
# course: CMPS3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 3/30/23
# Student 1: Michael Kausch
# Student 2: David Mesa
# Student 3: Irvin Neri Zavala
# Student 4: Samantha Tellez
# Student 5: Raul Verduzco Guillen
# description: Implementation Basic Data Analysis Routines
"""

# TODO:
#   - Data Structure for holding whether column vals are strings or floats
#   - this should coincide with the excel spreadsheet as well?



import pandas as pd
import time
import os
from datetime import datetime
import math
import re

def counts(data):
    count = 0
    # loop through data add one per row in data
    for row in data:
        count += 1
    print("Count: " ,  count)

def uniqueCounts(data):

    unique_set = set()
    # loop through data and store if was not previously found
    for unique in data:
        if not pd.isna(unique) and unique not in unique_set:
            unique_set.add(unique)
    print("Unique: " , len(unique_set))

# Standard Deviation and Variance 
def stanDev(data):
    # variables     
    stand_diff = set()
    mean = 0
    sum_sq = 0
    var = 0
    st_dev = 0

    # Step1: find the mean
    for index in data:
        mean += index
    mean = round(mean / len(data))

    # Step 2: find each deviation of the mean and square then add it to stand_diff list
    for index in data:
        stand_diff.add(math.pow((mean - index), 2))

    # Step3: sum of the stand_diff
    for sum_index in stand_diff:
        sum_sq += sum_index

    # Step 4: variance and sqrt to get stdev   
    var = (round(sum_sq/ (len(data)-1),4))
    st_dev = math.sqrt(var)

    # print statements
    print("Mean: ", mean)
    print("STDEV: ", round(st_dev, 4))
    print("Variance: ", var)
    # had two functions but you need to find the variance to find the stdev, so just merged the
    # two functions

def maxFunc(data):
    #initialize max for string and int/float, plus dict.
    max_num = None
    max_string = None
    string_dict = {}

    for temp in data:
        #made a bool to determine if int/float being used
        int_float = True
        for char in str(temp):
            if char not in ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                int_float = False
                break
        #ints/floats are dealt here
        if int_float:
            if max_num is None or temp > max_num:
                max_num = temp
        #strings are dealt here
        #finding max # of instances
        elif not int_float:
            if temp in string_dict:
                string_dict[temp] += 1
            else:
                string_dict[temp] = 1

    #set count to 0
    max_count = 0
    for string, str_count in string_dict.items():
        if str_count > max_count:
            max_count = str_count
            max_string = string

    if max_num is not None:
            print("Maximum: ", max_num)
            return max_num
    else:
            print("Maximum: ", max_string)
            return max_string

def minFunc(data):
    #initialize max for string and int/float, plus dict.
    min_num = None
    minstring = None
    string_dict = {}

    for temp in data:
        #made a bool to determine if int/float being used
        int_float = True
        for char in str(temp):
            if char not in ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                int_float = False
                break
        #ints/floats are dealt here
        if int_float:
            if min_num is None or temp < min_num:
                min_num = temp
        #strings are dealt here
        #finding max # of instances
        elif not int_float:
            if temp in string_dict:
                string_dict[temp] += 1
            else:
                string_dict[temp] = 1

    #this count needs to be a big #
    min_count = 1000000000
    for string, str_count in string_dict.items():
        if str_count < min_count:
            min_count = str_count
            min_string = string

    if min_num is not None:
        print("Minimum: ", min_num)
        return min_num
    else:
        print("Minimum: ", min_string)
        return min_string


def medianFunc(data):
    # make list for int, float, str, and date str
    int_list = []
    float_list = []
    str_list = []
    date_str_list = []
    
    # separate the ints/floats together
    # and the date str and other strings separately
    for temp in data:
        if isinstance(temp, int):
            int_list.append(temp)
        elif isinstance(temp, float):
            float_list.append(temp)
        elif isinstance(temp, str):
            try:
                datetime.strptime(temp, '%m/%d/%Y %I:%M:%S %p')
                date_str_list.append(temp)
            except ValueError:
                str_list.append(temp)

    # sort int and float numerically
    int_list.sort()
    float_list.sort()

    # sort string alphabetically and date str chronologically using datetime
    str_list.sort()
    date_str_list.sort(key=lambda s: datetime.strptime(s, '%m/%d/%Y %I:%M:%S %p'))

    # merge them all together
    merged_list = int_list + float_list + str_list + date_str_list

    # used to see if sorted correctly
    #print(merged_list)

    # find median
    length_list = len(merged_list)
    if length_list % 2 == 0:
        # when there is more then one median, chose median that is "smaller"
        temp1 = length_list // 2
        temp2 = temp1 - 1
        if isinstance(merged_list[temp1], str):
            median = sorted([merged_list[temp1], merged_list[temp2]])[0]
        else:
            median = (merged_list[temp1] + merged_list[temp2]) / 2
            # if float ends in .0, change to int
            if median.is_integer():
                median = int(median)
    else:
        # output median if there's only one
        tmp = length_list // 2
        median = merged_list[tmp]

    print("Median: ", median)

def modeFunc(data):
    # make list for int, float, str, and date str
    int_list = []
    float_list = []
    str_list = []
    date_str_list = []
    
    # separate the ints/floats together
    # and the date str and other strings separately
    for temp in data:
        if isinstance(temp, int):
            int_list.append(temp)
        elif isinstance(temp, float):
            float_list.append(temp)
        elif isinstance(temp, str):
            try:
                datetime.strptime(temp, '%m/%d/%Y %I:%M:%S %p')
                date_str_list.append(temp)
            except ValueError:
                str_list.append(temp)

    # sort int and float numerically
    int_list.sort()
    float_list.sort()

    # sort string alphabetically and date str chronologically
    str_list.sort()
    date_str_list.sort(key=lambda s: datetime.strptime(s, '%m/%d/%Y %I:%M:%S %p'))

    # merge them all together
    merged_list = int_list + float_list + str_list + date_str_list
    
    # used to see if sorted correctly
    #print(merged_list)

    # find mode
    count_dict = {}
    for cnt in merged_list:
        if cnt in count_dict:
            count_dict[cnt] += 1
        else:
            count_dict[cnt] = 1

    max_count = 0
    modes = []
    for itm, count in count_dict.items():
        if count > max_count:
            max_count = count
            modes = [itm]
        elif count == max_count:
            modes.append(itm)

    # for multiple ints, floats, strings, and dates choose smaller
    mode = modes[0]
    for multi in modes:
        if isinstance(multi, (int, float)):
            if multi < mode:
                mode = multi
        elif isinstance(multi, str):
            if multi < mode:
                mode = multi
        elif isinstance(multi, datetime):
            if multi < mode:
                mode = multi

    print("Mode: ", mode)

################################## BEGINNING OF DATA ANALYSIS ##################################
# def totalUniqueCountt(data):
#     nonp = time.time()
#     # create an empty dictionary to store unique crime counts per year
#     count_by_year = {}

#     # loop through each crime data
#     for index, row in data.iterrows():
#         # saves the year and crime into variables
#         year = int(row.year)
#         crime_code = row['Crm Cd']
        
#         # if the year and crime code combination is already in the dictionary, increment the count
#         if (year, crime_code) in count_by_year:
#             count_by_year[(year, crime_code)] += 1
#         # if the year and crime code combination is not in the dictionary, add it with a count of 1
#         else:
#             count_by_year[(year, crime_code)] = 1

#     # create a new dictionary to store unique crime counts per year, without considering the crime code
#     unique_counts_by_year = {}

#     # loop through each year and crime code combination in the dictionary
#     for (year, crime_code), count in count_by_year.items():
#         # if the year is already in the new dictionary, increment the count
#         if year in unique_counts_by_year:
#             unique_counts_by_year[year] += 1
#         # if the year is not in the new dictionary, add it with a count of 1
#         else:
#             unique_counts_by_year[year] = 1

#     # sort the dictionary by value in descending order and return it 0 for year 1 for count
#     sorted_counts = sorted(unique_counts_by_year.items(), key=lambda x: x[0], reverse=True)
#     for year, count in sorted_counts:
#         print(f"{year}: {count} unique crimes")
#     nonpend = time.time()
#     print("time:", (nonpend - nonp,"sec."))

def totalUniqueCount(filename):
    pandbegin = time.time()
    # group data by year and count unique crimes
    counts_by_year = filename.groupby('year')['Crm Cd'].nunique()
    
    # sort the counts in descending order and return them
    sorted_counts = sorted(counts_by_year.items(), key=lambda x: x[0], reverse=True)
    for year, count in sorted_counts:
        print("{}: Total Unique Crimes {}".format(year, count))
    pandtimeend = time.time()
    print("pandas time:", (pandtimeend - pandbegin),"sec.")

# def countCrimesByArea(data):
#     # create a nested dictionary to store the count of each area name for each year
#     nonp = time.time()
#     count_by_year_area = {}
#     for index, row in data.iterrows():
#         year = row['year']
#         area_name = row['AREA NAME']
#         if year not in count_by_year_area:
#             count_by_year_area[year] = {}
#         if area_name not in count_by_year_area[year]:
#             count_by_year_area[year][area_name] = 1
#         else:
#             count_by_year_area[year][area_name] += 1
    
#     # create a list to store the top 5 areas for each year
#     top_5_areas = []
    
#     # loop through each year
#     for year in count_by_year_area:
#         # create a list of tuples containing the area name and its count for the current year
#         areas_and_counts = []
#         for area_name, count in count_by_year_area[year].items():
#             areas_and_counts.append((area_name, count))
        
#         # sort the list using a bubble sort algorithm
#         n = len(areas_and_counts)
#         for i in range(n):
#             for j in range(0, n-i-1):
#                 if areas_and_counts[j][1] < areas_and_counts[j+1][1]:
#                     areas_and_counts[j], areas_and_counts[j+1] = areas_and_counts[j+1], areas_and_counts[j]
        
#         # append the top 5 areas to the result list
#         top_5_areas.append((year, areas_and_counts[:5]))
    
#     # print the result
#     for year, areas in top_5_areas:
#         print(f"{year}:")
#         for i, (area_name, count) in enumerate(areas):
#             print(f"{i+1}. {area_name}: {count} crimes")
#         print()
#     nonpend = time.time()
#     print("time:", (nonpend - nonp,"sec."))

def countCrimesByArea(data):
    begin = time.time()
    # group data by area name and count crimes
    counts_by_area = data.groupby('AREA NAME')['Crm Cd'].count()
    
    # sort the counts in descending order and return the top 5
    top_5_areas = counts_by_area.sort_values(ascending=False)[:5]
    
    # print the results
    for area, count in top_5_areas.items():
        print(f"{area}: {count} crimes")
       
    end = time.time()
    print("time:", (end - begin,"sec."))

def MonthsUniqueCrimes(data):
    # Convert the date column to datetime format
    data['DATE OCC'] = pd.to_datetime(data['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')
    
    # Group the data by month and count unique crimes
    counts_by_month = data.groupby(data['DATE OCC'].dt.strftime('%B'))['Crm Cd'].nunique()
    
    # Sort the counts in ascending order and return them
    sorted_counts = sorted(counts_by_month.items(), key=lambda x: x[1])
    for month, count in sorted_counts:
        print("{}: Total Unique Crimes {}".format(month, count))

# def Top10Streets(data):
    # # Filter data for 2019
    # la_crime_data = data.loc[(data["year"] == 2019) & (data["LOCATION"] == "Los Angeles")]

    # # group the data by street name and count the number of crimes
    # crime_by_street = la_crime_data.groupby("Cross Street")["crime"].count().reset_index(name="count")

    # # sort the data by the count of crimes (in descending order) and select the top 10
    # top_10_streets = crime_by_street.sort_values("count", ascending=False).head(10)

    # # display the top 10 streets and their crime counts
    # print("Top 10 streets with the most crimes in LA in 2019:")
    # for i, row in top_10_streets.iterrows():
    #     print(f"{i+1}. {row['street']}: {row['count']} crimes")

    # # display the total number of crimes in each street
    # crime_totals_by_street = crime_by_street.groupby("street")["count"].sum().reset_index(name="total_count")
    # print("\nTotal crimes in each street:")
    # for i, row in crime_totals_by_street.iterrows():
    #     print(f"{row['street']}: {row['total_count']} crimes")

# def Top5HWood(data):
    
    # # filter for Hollywood
    # hollywood_crimes = data[data['AREA NAME'] == 'Hollywood']

    # # extract the hour of the crime
    # hollywood_crimes['TIME OCC'] = pd.to_datetime(hollywood_crimes['TIME OCC'], format='%H%M').dt.hour

    # # group by hour and count the number of crimes
    # hourly_crime_counts = hollywood_crimes.groupby('TIME OCC')['DR_NO'].count()

    # # sort the counts in descending order
    # sorted_crime_counts = hourly_crime_counts.sort_values(ascending=False)

    # # display the top 5 most dangerous hours and their crime counts
    # print(sorted_crime_counts.head(5))

def MostTime(data):
      # Convert the date columns to datetime type
    data['DATE OCC'] = pd.to_datetime(data['DATE OCC'])
    data['Date Rptd'] = pd.to_datetime(data['Date Rptd'])

    # Calculate the time difference in hours for all crimes using vectorized operations
    time_diff_hours = (data['Date Rptd'] - data['DATE OCC']).dt.total_seconds() / 3600

    # Get the index of the crime with the maximum time difference
    max_time_index = time_diff_hours.idxmax()

    # Get the crime with the maximum time difference using the index
    max_time_crime = data.loc[max_time_index]

    # Print the details of the crime with the maximum time difference
    print(f"Crime with maximum time difference:\n{max_time_crime}")

def printMostCommonCrime(data):
     # Count the occurrences of each crime type
    crime_counts = data.groupby('Crm Cd Desc').size().sort_values(ascending=False)

    # Select the top 10 most frequent crime types
    top_crime_types = crime_counts.head(10)

    # Print the results
    for i, (crime_type, count) in enumerate(top_crime_types.iteritems()):
        print(f"{i+1}. {crime_type}: {count}")

def OlderManTop5(data):
 # Filter data for December 2018 and older male victims
    filtered_data = data[(data['DATE OCC'] >= '12/01/2018') & (data['DATE OCC'] <= '12/31/2018') & (data['Vict Age'] >= 65) & (data['Vict Sex'] == 'M')]
    # Count the occurrences of crimes in each area
    area_counts = filtered_data.groupby('AREA NAME').size().sort_values(ascending=False)
    test = filtered_data.groupby('AREA NAME').size()
    heapTest = heapSort(test)

    # Select the top 5 most dangerous areas for older men
    top_areas = area_counts.head(5)
    test_areas = test.head(5)
    # Print the results
    for i, area in enumerate(top_areas.index):
        print(f"{i+1}. {area} ({top_areas[area]} incidents)")

    for i, tarea in enumerate(test_areas.index):
        print(f"{i+1}. {tarea} ({test_areas[tarea]} test incidents)")
################################## END OF DATA ANALYSIS ##################################
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def getPrintColumns(dframe):
    headers = list(dframe.columns)
    print(headers)

#Time to read and store data in an array

def readFile(file_name="Crime_Data_from_2017_to_2019.csv"):
    # s_time = time.time()
    csv_arr = pd.read_csv(file_name, quotechar='"', delimiter=',', skipinitialspace=True, dtype = {"Date Rptd":"string", "year": "int32"} )
    drop_columns = ['Unnamed: 0', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street']
    csv_arr.drop(drop_columns, axis= 1, inplace = True)
    
    headers = list(csv_arr.columns)
    #rows = df.index.values
    result = csv_arr.dtypes

    print(f"[{len(csv_arr)} rows x {len(headers)} columns]")
    print("#     Column    \tNon-null\tDtype")
    print("---   ----------\t-----------\t------")

    num_na = dict()
    num_duplicates = dict()
    num_na_list = []


    for header in headers:
        num_na[header] = csv_arr[header].isna().sum()
        #print(f"{header}: {num_na[header]}")
    for ind in num_na.keys():                                                          # add the sum of Na of each header to a list to print later
        num_na_list.append(num_na[ind])

    for header in headers:
        num_duplicates[header] = csv_arr.duplicated(subset=header).sum()
        #print(f"{header}: {num_duplicates[header]}") 

    for i in range(len(headers)):                                                       # print table of the loaded data
        #print(f"{i}\t{headers[i]}\t\t{num_na_list[i]}\t{result[i]}")
        print('%-5s'%i, '%-20s'%headers[i], '%-12s'%(len(csv_arr) - num_na_list[i]), '%-15s'%result[i])

    # declare each types to find the sum of each
    float_sum = 0
    int_sum = 0
    int32_sum = 0
    object_sum = 0
    string_sum = 0

    # loop through and count each type
    for i in range(len(headers)):
            if result[i] == "float64":
                float_sum += 1
            elif result[i] == "int64":
                int_sum += 1
            elif result[i] == "int32":
                int32_sum += 1
            #elif result[i] == "string":
                #print(result[i])
                #print("test")
                #string_sum += 1
                #print("test")
            elif result[i] == "object":
                object_sum += 1
    # print the sum of each type from the data            
    print(f"dtypes: float64({float_sum}),  int32({int32_sum}),  int64({int_sum}),  object({object_sum}), string({string_sum})")
    print(f"Memory Usage:     \n")

    # print("Read time: ", (e_time-s_time), "\n")
    #csv_arr.drop(csv_arr.columns[[28,22]], axis=1, inplace=True)

    #for i in range(len(headers)):
    #    if num_na_list[i] >> 0:
    #        print(i)
    #        csv_arr = csv_arr.drop(csv_arr.columns[[i]], axis= 1, inplace= True)
     # dropping columns Crm Cd 2,Crm Cd 3, Crm Cd 4, Cross Street due to having a high rate of null values
    #csv_arr.drop(['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street'], axis= 1, inplace= True)
    #csv_arr = csv_arr.drop_duplicates(subset='Cm Cd 1', keep="first")
    #csv_arr.drop_duplicantsi

    return(csv_arr)


    # s_time = time.time()
    #csv_arr = pd.read_csv(file_name, quotechar='"', delimiter=',', skipinitialspace=True)    
    # e_time = time.time()
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
    #headers = list(csv_arr.columns)
    
    #result = csv_arr.dtypes
    #for i in range(len(headers)):
    #    print(f"{headers[i]}: {result[i]}")
    
    # print("Read time: ", (e_time-s_time), "\n")
    
  
    #num_na = dict()
    #num_duplicates = dict()
    
    #print("header  --  #NAN")
    #for header in headers:
    #    num_na[header] = csv_arr[header].isna().sum()
    #    print(f"{header}: {num_na[header]}")
        
    #print(f"\n\nheader  --  #duplicates")

    #for header in headers:
    #    num_duplicates[header] = csv_arr.duplicated(subset=header).sum()
    #    print(f"{header}: {num_duplicates[header]}")
    
    #return(csv_arr)


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


def sortData(dframe, column_name):
    ''' method for sorting data frame data by passed in column_name'''
    pass

    # def sortData(dframe, column_name):
#     ''' method for sorting data frame data by passed in column_name'''
#     heapSort()

def heapify(lst, i, upper):
    while (True):
        l, r = i*2+1, i*2+2

        # 2 children
        if (max(l,r) < upper):
            if (lst[i] >= max(lst[l], lst[r])):
                break
            elif (lst[l] > lst[r]):
                lst[l], lst[i] = lst[i], lst[l]
                i = l
            else:
                lst[r], lst[i] = lst[i], lst[r]
                i = r
                
        # 1 child
        elif (l < upper):
            if lst[l] > lst[i]:
                lst[l], lst[i] = lst[i], lst[l]
                i = l
            else:
                break
        elif (r < upper):
            if lst[r] > lst[i]:
                lst[r], lst[i] = lst[i], lst[r]
                i = r
            else:
                break
        # no children
        else:
            break
  
# The main function to sort an array of given size
  
def heapSort(lst):
    for itm in range(len(lst)-2//2, -1, -1):
        heapify(lst, itm, len(lst))
    
    for end in range(len(lst)-1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        heapify(lst, 0, end)
    
    # search(data_frame, col_number, search_ele)


def describeColumn(data_list, col_number, data_bools):
    # TODO
    counts(data_list)
    uniqueCounts(data_list)

    # # only call STDEV and Variance when needed
    # if (col_number  == 4 or col_number==12 or 27 <= col_number <= 29  ):
    #     stanDev(data_list);
    #     # variance(data_list);
        
    if (data_bools[col_number]["mean"] == True):
        stanDev(data_list)
    else:
        print("Mean: N/A")
        print ("STDEV: N/A")
        print ("Variance: N/A")
        
    if (data_bools[col_number]["median"] == True):
        medianFunc(data_list)
    else:
        print("Median: N/A") 
        
    if (data_bools[col_number]["mode"] == True):
        modeFunc(data_list)
    else:
        print("Mode: N/A")

    # if (data_bools[col_number]["stdev"] == True):
    #     stanDev(data_list)
    # else:
    #     print ("Standard Deviation: N/A")
    #     print ("Variance: N/A")
       
    if (data_bools[col_number]["min"] == True):
        minFunc(data_list)
    else:
        print("Minimum: N/A")

    if (data_bools[col_number]["max"] == True):
        maxFunc(data_list)
    else:
        print("Maximum: N/A")

    # if (data_bools[col_number]["var"] == True):
    #     variance(data_list)
    # else:
    #     print ("Variance: N/A")


   # print(data_list)
    
    pass

def printDataset(data_frame, num_rows):
    pd.set_option('display.max_columns', None)
    print(data_frame.iloc[:num_rows])
    
    date_time = datetime.now()
    dts = date_time.strftime("%y%m%d%H%M%S_data_print.csv")
    print("Data was written to ((", dts, "))")
    data_frame.iloc[:num_rows].to_csv(dts)
    pd.reset_option("max_columns")
    
    
def getResponse(foo, min_val, max_val, **kwargs):
    '''Takes in a print function (foo) and tests against minumum
        and maximum menu options.
        Function returns an integer value that met the response criteria
        if function foo takes parameters (like a list), they are included as a key word
        argument arg_list'''
    response = -2
    
    if 'arg_list' not in kwargs:
        pass
    
    # if 'arg_list' in kwargs:
    #     print(f"you passed in an arg_list:")
    #     print(f"{kwargs.get('arg_list')}")
    
    while ((response < min_val) or (response > max_val)):
        # foo()
        
        try:
            str_response = input("Enter your response: ")
            response = int(str_response)
            
            if ((response < min_val) or (response > max_val)):
                #os.system('clear')
                clear()
                if 'arg_list' in kwargs:
                    foo(kwargs.get('arg_list'))
                else:
                    foo()
                print(response, "is not in the range of acceptable values.")
                print("Enter a value between", min_val, "and", max_val)
        except:
            #os.system('clear')
            clear()
            
            if 'arg_list' in kwargs:
                foo(kwargs.get('arg_list'))
            else:
                # print('arg list not found so calling reg foo()')
                # input()
                foo()
                
            print(str_response, "is not a valid response. Please enter an integer.")
            response = -2
        
    return response


# searches a specified data_frame column for a user inputed string/integer
def search(data_frame, col_num, search_string):
    row_match = []
    found = False
    col_name = data_frame.columns[col_num]
    
    for index, row in data_frame.iterrows():
        if(re.search(search_string, str(row[col_name]), re.IGNORECASE)):
            row_match.append(index)
        
    if len(row_match) != 0:
        found = True
        print(data_frame.loc[row_match])
            
            
    return found
            
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
    # print("25. Add Back a Dropped Column:")
    print("25. Back to the Main Menu")
        

def printDropHeaders(header_list):
    printHeaders(header_list)
    print("Enter a column number to drop")
    print("Enter -1 to finish entering columns")
    

def printDayPrompt():
    print("What day do you want to search?")

def printMonthPrompt():
    print("What month do you want to search? ")
    
def printYearPrompt():
    print("What year do you want to search?")
    
# def printInclHeaders(incl_header_list):
#     printHeaders(incl_header_list)
#     print("Enter a column number to add")
#     print("Enter -1 to finish entering columns")    
   
def printHeaders(header_list):
    for i in range(len(header_list)):
        print(f"[{i}] {header_list[i]}")
    
def printDescribeColMenu(incl_header_list):
    print("Describe Columns:")
    print("*****************")
    print("*****************")
    printHeaders(incl_header_list)
    print("Enter the column number to desribe")
    # print("Enter -1 to finish entering columns")    
    
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
    totalUniqueCount(df)
    # totalUniqueCountt(df)
    print(f"\nShow the top 5 areas with the most crime events in all years:")
    countCrimesByArea(df)
    print("\nShow all months and the unique total count of crimes sorted in increasing order.")
    MonthsUniqueCrimes(df)
    print("\nShow the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.")
    # Top10Streets(df) # TODO
    print("\nShow the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.")
    #Top5HWood(df) # TODO
    print("\nPrint the details of the crime that that took the most time (in hours) to be reported.")
    # MostTime(df) # Done but need optimized
    print("\nShow the 10 top most common crime types (Crm Cd Desc) overall across all years.")
    printMostCommonCrime(df) 
    print("\nAre woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.")
    # printLALunchTime(df) # TODO
    print("\nWhat is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.")
    # printCCFrauds(df) # TODO
    print("\nList the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.")
    OlderManTop5(df) # TODO
    print(df)

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
    # included_headers = []
    # excluded_headers = []
    all_headers = []
    data_frame_bak = None
    
    data_bools_unmod = [
                    # dict(count=True, unique_count=True, mean=False, median=True, mode=True, stdev=False, var=False, min=True, max=True), #0
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
                    # dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #22
                    # dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #23
                    # dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #24
                    dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #25
                    # dict(count=True, unique_count=True, mean=False, median=False, mode=True, stdev=False, var=False, min=False, max=False), #26
                    
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #27
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #28
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True)] #29
    data_bools = data_bools_unmod.copy()
    
    
    while (menu_option != 5):
        #os.system("clear")
        clear()
        if (error_msg != ""):
            print(error_msg)
            error_msg = ""
        
        printBaseMenu()
        menu_option = getResponse(printBaseMenu, 1, 5)
        # print("you selected option", menu_option)   #debug
        
        
        if (menu_option== 1):
            #os.system("clear")
            clear()
            menu_list = getCsvFileList()
            printDataSelectMenu(menu_list)
            sub_menu_option = getResponse(printDataSelectMenu, 1, len(menu_list), arg_list=menu_list)
            # print("calling readFile on",menu_list[sub_menu_option-1])
            print("")
            
            try:
                s_time = time.time()
                data_frame = readFile(menu_list[sub_menu_option-1])
                data_frame_bak = data_frame.copy()
                e_time = time.time()
                print("[start time]", s_time)
                print("[end time]", e_time)
                print("Time to load:", (e_time-s_time),"sec.")
                all_headers = list(data_frame.columns)
                data_bools = data_bools_unmod.copy()
                # included_headers = all_headers.copy() # save backup of all column names
                # print("included headers:")
                # print(included_headers)
                print(f"\nTotal Columns Read: {len(all_headers)}")
                print(f"Total Rows Read: {len(data_frame.index)}")
                # print(f"\nTotal Elements (Not null) in each category:\n\n{data_frame.notna().sum()}")
                
            except:
                error_msg = f"could not load data file {menu_list[sub_menu_option-1]}"

            input("press enter to continue...")
            continue
            
        elif (menu_option == 2):
            # Explore Data
            #os.system("clear")
            clear()
            if (data_frame.empty):
                error_msg = """You haven't loaded any data yet!
                Select option 1 from the main menu"""
                continue
            
            # print("Data Exploration Section")
            sub_menu_option = 0
            print_msg = ""
            while (sub_menu_option != 25):
                # get user input until correct
                #os.system("clear")
                clear()
                if (print_msg != "" ):
                    print(print_msg)
                    print_msg = ""
                printDataExpMenu()
                sub_menu_option = getResponse(printDataExpMenu, 21, 25)
                col_number = 0

                if (sub_menu_option == 21):
                    # list all columns
                    clear()
                    print("*****************")
                    print(f"Data Columns:\n")
                    print("*****************")
                    printHeaders(all_headers)
                    print("*****************")
                    print("*****************")
                    # print("*****************")
                    # print("*****************")
                    # print("Included Columns:")
                    # print("*****************")
                    # if (len(included_headers) > 0):
                    #     printHeaders(included_headers)
                    # else:
                    #     print("No columns are currently included")
                    # print("*****************")
                    # print("*****************")
                    # print("Excluded Columns:")
                    # print("*****************")
                    # if (len(excluded_headers) > 0):
                    #     printHeaders(excluded_headers)
                    # else:
                    #     print("No columns are currently excluded")
                    # print("*****************")
                    # print("*****************")
                    input(f"\npress enter to continue...")
                    continue
                    
                elif (sub_menu_option == 22):
                    # Drop Columns
                    #clear()
                    while (col_number != -1):
                        clear()
                        
                        
                        printDropHeaders(all_headers)
                        col_number = getResponse(printDropHeaders, -1, len(all_headers)-1, arg_list=all_headers)
                        # print("col_number now",col_number)
                        
                        if (col_number != -1):
                            # excluded_headers.append(included_headers[col_number])
                            # print(f"excluded headers last: {excluded_headers[-1]}")
                            # included_headers.remove(included_headers[col_number])
                            data_frame.drop(columns = [all_headers[col_number]], inplace=True)
                            print(f"\nColumn {all_headers[col_number]}\n")
                            all_headers = list(data_frame.columns)
                            data_bools.pop(col_number)
                            input(f"\nwas successfully dropped. Press any key...")
                            
                            # print("included_headers now***")
                            # print(all_headers)
                        
                        
                          
                    print("Finished removing columns")
                    print(f"There are currently {len(all_headers)} columns of data included.")
                    input("press any key to continue...")
                    col_number = 0
                    
                elif (sub_menu_option == 23):
                    # Desribe Columns
                    # input("describing the columns..")
                    clear()
                    
                    printDescribeColMenu(all_headers)
                    col_number = getResponse(printDescribeColMenu, -1, len(all_headers)-1, arg_list=all_headers)
                    if (col_number == -1):
                        col_number = 0
                        continue
                    
                    # TODO: function to retrieve all of the stats: describeColumn
                    #  - return dictionary of count, unique, mean, median, mode, stdev, variance, minimum, maximum

                    # datalst = data_frame[all_headers[col_number]].to_list()
                    
                    clean_df = data_frame.dropna(axis = 'index', subset = all_headers[col_number])
                    
                    # clean out 0.0's from lat and long columns
                    if (all_headers[col_number] == 'LAT' or all_headers[col_number] == 'LON'):
                        clean_df = clean_df[clean_df[all_headers[col_number]] != 0]
                        
                    if (all_headers[col_number] == 'Vict Age'):
                        clean_df = clean_df[clean_df[all_headers[col_number]] > 0]
                        # print("should have cleaned neg values from vic age")
                    
                    clean_lst = clean_df[all_headers[col_number]].to_list()
                    
                    # fin = open("log.log", "w")
                    # for val in clean_lst:
                    #     # print(val)
                    #     fin.write(str(val) + '\n')
                    # fin.close()
                    print(f"{all_headers[col_number]} stats:")
                    print("============================")
                    

                    try:
                        s_time = time.time()
                        # describeColumn(datalst, col_number, data_bools)
                        describeColumn(clean_lst, col_number, data_bools)
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
                    clear()
                    printSearchMenu(all_headers)
                    col_number = getResponse(printSearchMenu, -1, len(all_headers)-1, arg_list=all_headers)
                    month = 0
                    day = 0
                    year = 0
                    # year_list = data_frame_bak['year'].to_list()
                    # min_year = int(minFunc(year_list))
                    # max_year = int(maxFunc(year_list))
                    # max_day = None
                    search_ele = None
                    # print("min_year:", min_year, "max_year:", max_year)
                    # input("enter anything")
                    
                    
                    if (col_number == -1):
                        col_number = 0
                        continue
                    
                    if (all_headers[col_number] == 'Date Rptd' or all_headers[col_number] == 'DATE OCC'):
                        # print ("we're looking at a date here mike")
                        printYearPrompt()
                        year = getResponse(printYearPrompt, 1900, 2023)
                        printMonthPrompt()
                        month = getResponse(printMonthPrompt, 1, 12)
                        # months_31 = [1, 3, 5, 7, 8, 10, 12]
                        # months_30 = [4, 6, 9, 11]
                        # if (month in months_31):
                        #     # print("month had 31 days")
                        #     max_day = 31
                        # elif (month in months_30):
                        #     # print("month had 30 days")
                        #     max_day = 30
                        # else:
                        #     print("month was february")
                        #     max_day = 29
                        printDayPrompt()
                        day = getResponse(printDayPrompt,1, 31)
                        
                        m_str = str(month).rjust(2, '0')
                        d_str = str(day).rjust(2, '0')
                        print("searching the following string...")
                        # print(m_str + '/' + d_str + '/' + str(year))
                        search_ele = str(m_str + '/' + d_str + '/' + str(year))
                        print(search_ele)
                    else:
                        search_ele = input("Enter the search value: ")
                    
                    # TODO: Need to make 1:1 list of variable type so that I can 
                    #       check and see if the correct element was input
                    

                    is_found = False
                    s_time = time.time()
                    # should return a bool
                    is_found = search(data_frame, col_number, search_ele) # TODO: search function
                    
                    datalst = data_frame[all_headers[col_number]].to_list()

                    
                    e_time = time.time()
                    
                    
                    if (is_found):
                        print("Data found!")
                        print("Time to process is", (e_time-s_time),"sec.")
                    else:
                        print(f"could not locate (({search_ele})) in the data")
                        print("Total search time was", (e_time-s_time),"sec.")
                    
                    input("Press any key to continue")
                    continue
                    
                # elif (sub_menu_option == 25):
                #     # add back a dropped column
                #     # input("adding back a dropped column...")
                #     # Drop Columns
                #     clear()
                     
                #     if (len(excluded_headers) == 0):
                #         print_msg = "There are currently 0 excluded columns so there's none to add back!"
                #         continue
                     
                #     while (col_number != -1):
                #         printInclHeaders(excluded_headers)
                #         col_number = getResponse(printInclHeaders, -1, len(excluded_headers)-1, arg_list=excluded_headers)
                #         # print("col_number now",col_number)
                        
                #         if (col_number != -1):
                            
                #             included_headers.append(excluded_headers[col_number])
                #             # print(f"included headers last: {included_headers[-1]}")
                #             excluded_headers.remove(excluded_headers[col_number])
                #             # print("excluded_headers now***")
                #             # print(excluded_headers)
                            
                #     print("Finished adding back columns")
                #     print(f"There are currently {len(excluded_headers)} items still being excluded.")
                #     col_number = 0
                #     input("press any key to continue...")
                    
                elif (sub_menu_option == 25):
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
            
            printDataAnalysis(data_frame_bak)
            
            input("Press any key to continue...")
            continue
        elif (menu_option == 4):
            # Print Data Set
            if (data_frame.empty):
                error_msg = """You haven't loaded any data yet! 
                Select option 1 from the main menu"""
                continue
            clear()
            num_rows = [100, 1000, 5000]
            printMenu()
            sub_menu_option = getResponse(printMenu, -1, 3)
            
            print(f"printing {num_rows[sub_menu_option]} number of rows...\n")
            printDataset(data_frame, num_rows[sub_menu_option]) # TODO
            # print("done printing")
            # print("data also appended to dataout.txt")
            input("Press any key to continue...")
            
            # error_msg = "Print Data Section"
            continue
        
            # Prints specific rows in array:
            # print(data_frame[0:9])
            # print(data_frame.loc[0:9,"DR_NO"])
            # data_frame.to_csv('output.csv',)
            
        
if __name__ == '__main__':
    #os.system('clear')
    clear()
    main()
