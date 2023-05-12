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
import calendar

def counts(data):
    count = 0
    # loop through data add one per row in data
    for row in data:
        count += 1
    # print("Count: " ,  count)
    return count

def uniqueCounts(data):
    # isDate = True
    unique_set = set()
    # loop through data and store if was not previously found
    for unique in data:
        if not pd.isna(unique):
            if isinstance(unique, str):
                try:
                    datetime.strptime(unique, '%m/%d/%Y %I:%M:%S %p')
                    # date_str_lst.append(temp)
                except ValueError:
                    # str_lst.append(temp)
                    # print(unique, "not a date")
                    pass

            if unique not in unique_set:
                unique_set.add(unique)
                # print(unique, "being added")
            
        # if not pd.isna(unique) and unique not in unique_set:
        #     unique_set.add(unique)
    # print("Unique: " , len(unique_set))
    return len(unique_set)

# Standard Deviation and Variance 
def stanDev(data):
    # variables
    
    # print("about to make stats dict")  
    stats = {'mean': 0, 'var': 0, 'st_dev': 0}
    # print("done making stats dict")
    stand_diff = set()
    # stats['mean'] = 0
    sum_sq = 0
    # stats['var'] = 0
    # stats['st_dev'] = 0


    # Step1: find the stats['mean']
    # print("getting mean")
    for index in data:
        stats['mean'] += index
    stats['mean'] = round(stats['mean'] / len(data))

    # Step 2: find each deviation of the stats['mean'] and square then add it to stand_diff list
    # print("getting stand_diff")
    for index in data:
        stand_diff.add(math.pow((stats['mean'] - index), 2))

    # Step3: sum of the stand_diff
    # print("getting sum_sq")
    for sum_index in stand_diff:
        sum_sq += sum_index

    # Step 4: variance and sqrt to get stdev  
    # print("calculating variance")
    stats['var'] = (round(sum_sq/ (len(data)-1),4))
    # print("calculating st_dev")
    stats['st_dev'] = math.sqrt(stats['var'])

    # print statements
    # print("Mean: ", stats['mean'])
    # print("STDEV: ", round(stats['st_dev'], 4))
    # print("Variance: ", stats['var'])
    # had two functions but you need to find the variance to find the stdev, so just merged the
    # two functions
    return stats

def maxFunc(data):
    # make individ lists
    int_lst = []
    flt_lst = []
    str_lst = []
    date_str_lst = []

    # separate ints and floats / date str and str
    for temp in data:
        if isinstance(temp, int):
            int_lst.append(temp)
        elif isinstance(temp, float):
            flt_lst.append(temp)
        elif isinstance(temp, str):
            try:
                datetime.strptime(temp, '%m/%d/%Y %I:%M:%S %p')
                date_str_lst.append(temp)
            except ValueError:
                str_lst.append(temp)

    # find max int
    max_num = None
    if int_lst:
        max_num = int_lst[0]
        for i in range(1, len(int_lst)):
            if int_lst[i] > max_num:
                max_num = int_lst[i]

    # find max flt
    if flt_lst:
        if max_num is None or flt_lst[0] > max_num:
            max_num = flt_lst[0]
        for i in range(1, len(flt_lst)):
            if flt_lst[i] > max_num:
                max_num = flt_lst[i]

    # find max str
    max_str = None
    if str_lst:
        max_str = str_lst[0]
        for i in range(1, len(str_lst)):
            if str_lst[i] > max_str:
                max_str = str_lst[i]

    # find max date
    max_date_str = None
    if date_str_lst:
        max_date_str = date_str_lst[0]
        for i in range(1, len(date_str_lst)):
            if datetime.strptime(date_str_lst[i], '%m/%d/%Y %I:%M:%S %p') > datetime.strptime(max_date_str, '%m/%d/%Y %I:%M:%S %p'):
                max_date_str = date_str_lst[i]

    if max_str is not None:
        print("Maximum: ", max_str)
    elif max_num is not None:
        print("Maximum: ", max_num)
    else:
        print("Maximum: ", max_date_str)

def medianFunc2(data):
    '''Takes in a sorted list and returns middle value'''
    mid = int((len(data)/2))
    # print("mid is", mid)
    return data[mid]

def minFunc2(data):
    '''data: a list sorted in ascending order'''
    return data[0]

def maxFunc2(data):
    '''data: a list sorted in ascending order'''
    return data[-1]

def minFunc(data):
    # make individ lists
    int_lst = []
    flt_lst = []
    str_lst = []
    date_str_lst = []

    # separate ints and floats / date str and str
    for temp in data:
        if isinstance(temp, int):
            int_lst.append(temp)
        elif isinstance(temp, float):
            flt_lst.append(temp)
        elif isinstance(temp, str):
            try:
                datetime.strptime(temp, '%m/%d/%Y %I:%M:%S %p')
                date_str_lst.append(temp)
            except ValueError:
                str_lst.append(temp)

    # find max int
    min_num = None
    if int_lst:
        min_num = int_lst[0]
        for i in range(1, len(int_lst)):
            if int_lst[i] < min_num:
                min_num = int_lst[i]

    # find max flt
    if flt_lst:
        if min_num is None or flt_lst[0] < min_num:
            min_num = flt_lst[0]
        for i in range(1, len(flt_lst)):
            if flt_lst[i] < min_num:
                min_num = flt_lst[i]

    # find max str
    min_str = None
    if str_lst:
        min_str = str_lst[0]
        for i in range(1, len(str_lst)):
            if str_lst[i] < min_str:
                min_str = str_lst[i]

    # find max date
    min_date_str = None
    if date_str_lst:
        min_date_str = date_str_lst[0]
        for i in range(1, len(date_str_lst)):
            if datetime.strptime(date_str_lst[i], '%m/%d/%Y %I:%M:%S %p') < datetime.strptime(min_date_str, '%m/%d/%Y %I:%M:%S %p'):
                min_date_str = date_str_lst[i]

    if min_str is not None:
        print("Minimum: ", min_str)
    elif min_num is not None:
        print("Minimum: ", min_num)
    else:
        print("Minimum: ", min_date_str)

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

def modeFunc2(sorted_list):
    '''takes in a sorted list of data in its correct format'''
    data = dict()
    for item in sorted_list:
        data[item] = data.get(item,0) + 1
        # print(item, ":", data[item])
    
    sorted_data = sorted([(v,k) for (k,v) in data.items()], reverse=True)
    # print("mode is:", sorted_data[0][1])
    return sorted_data[0][1]    
    

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
    return mode

################################## BEGINNING OF DATA ANALYSIS ##################################


def totalUniqueCount(filename):
    now = datetime.now()
    #pandaBegin = time.time()
    # group data by year and count unique crimes
    countsByYear = filename.groupby('year')['Crm Cd'].nunique()
    
    # sort the counts in descending order and return them
    sortedCounts = sorted(countsByYear.items(), key=lambda x: x[0], reverse=True)
    for year, count in sortedCounts:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] ""{}: Total Unique Crimes {}".format(year, count))
    #pandaTimeEnd = time.time()
    #print("Time:", (pandaTimeEnd - pandaBegin),"sec.")


def countCrimesByArea(data):
    now =datetime.now()
    #begin = time.time()
    # group data by area name and count crimes
    countsByArea = data.groupby('AREA NAME')['Crm Cd'].count()
    
    # sort the counts in descending order and return the top 5
    top5Areas = countsByArea.sort_values(ascending=False)[:5]
    
    # print the results
    
    for area, count in top5Areas.items():
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] {area}: {count} crimes")
       
    #end = time.time()
    #print("Time:", (end - begin,"sec."))

def MonthsUniqueCrimes(data):
    # copy data and add index locater
    dataCopy = data.copy()
    dataCopy = data.reindex(['DATE OCC', 'Crm Cd'], axis = 1)
    dataCopy.iloc[0,1]
    

    # Convert the date column to datetime format
    data['DATE OCC'] = pd.to_datetime(data['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')
    
    # Group the data by month and count unique crimes
    countsByMonth = data.groupby(data['DATE OCC'].dt.strftime('%B'))['Crm Cd'].nunique()
    
    # Sort the counts in ascending order and return them
    now = datetime.now()
    sortedCounts = sorted(countsByMonth.items(), key=lambda x: x[1])
    for month, count in sortedCounts:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] ""{}: Total Unique Crimes {}".format(month, count))

def Top10Streets(data):
    # Filter the data for the year 2019
    data2019 = data[data['year'] == 2019]

    # Count the occurrences of each street name
    streetCounts = data2019['LOCATION'].value_counts()

    # Select the top 10 streets with the most crimes
    topStreets = streetCounts.head(10)

    # Print the results
    now = datetime.now()
    for i, (street, count) in enumerate(topStreets.iteritems()):
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] {i+1}. {street}: {count} crimes")

def Top5HWood(data):
    now = datetime.now()
    
    # Filter the data to include only the specified area
    areaName = 'Hollywood'
    areaData = data[data['AREA NAME'] == areaName].copy() # make a copy of the slice
    areaData.loc[:, 'TIME OCC'] = pd.to_datetime(areaData['TIME OCC'].astype(str), format='%H%M', errors='coerce')
    
    # Count the number of crimes that occur in each hour of the day
    crimeCounts = areaData.groupby(areaData['TIME OCC'].dt.hour).size().sort_values(ascending=False)
    
    # Select the top n hours with the most crimes
    topHours = crimeCounts.head(5)
    
    # Print the results
    
    for i, (hour, count) in enumerate(topHours.iteritems()):
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] {i+1}: {int(hour):02d}:00 - {int(hour):02d}:59: {count} crimes")

def printCCFrauds(data):
    now = datetime.now()
    # Convert Date Rptd column to datetime format
    data["DATE OCC"] = pd.to_datetime(data["DATE OCC"], format="%m/%d/%Y %I:%M:%S %p")
    
    # Filter for major credit card frauds in 2019
    fraudData = data.loc[(data["Crm Cd Desc"] == "CREDIT CARDS, FRAUD USE ($950 & UNDER") & (data["year"] == 2019), :]

    if len(fraudData) == 0:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f'[{current_time}] No credit card frauds found in 2019')
        return

    # Extract month from DATE OCC column using .dt accessor
    fraudData = fraudData.assign(month=fraudData["DATE OCC"].dt.month)

    # Count the number of frauds by month
    fraudCountsByMonth = fraudData["month"].value_counts()

    # Find the month(s) with the most frauds
    maxFraudCount = fraudCountsByMonth.max()
    monthsWithMaxFraud = fraudCountsByMonth[fraudCountsByMonth == maxFraudCount].index
    monthNames = [calendar.month_name[m] for m in monthsWithMaxFraud]

    # Print the result
    if len(monthNames) == 1:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f'[{current_time}] The month with the most major credit card frauds in 2019 is {monthNames[0]}, with {maxFraudCount} frauds.')
    else:
        monthStr = " and ".join(monthNames)
        current_time = now.strftime("%H:%M:%S.%f")
        print(f'[{current_time}] The months with the most major credit card frauds in 2019 are {monthStr}, with {maxFraudCount} frauds each.')
    
    # Loop through all months and print out the fraud data for each month
    #For testing purposes
    # for month in range(1, 13):
    #     fraudDateForMonth = fraudData[fraudData["month"] == month]
    #     print(f"Month {month}: {len(fraudDateForMonth)} frauds")
    #     print(fraudDateForMonth.head())
       
def MostTime(data):
    now = datetime.now()
    dataCopy = data.copy()
    dataCopy.iloc[0,1]
  
    # Create a new column with the time difference between the report date and the date the crime occurred
    dataCopy['DATE OCC'] = pd.to_datetime(dataCopy['Date Rptd'], format='%m/%d/%Y %I:%M:%S %p') - pd.to_datetime(dataCopy['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')
    
    # Sort the DataFrame by the time difference column in descending order
    sortedData = dataCopy.sort_values(by='DATE OCC', ascending=False)
    
    # Get the details of the crime wit\nh the highest time difference
    maxReportTime = sortedData.iloc[0]
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"[{current_time}] Time difference in hours: {maxReportTime['DATE OCC'].total_seconds() / 3600}")
    # Print the details of the crime
    for key, value in maxReportTime.to_dict().items():
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] {key}: {value}")

def printMostCommonCrime(data):
    now = datetime.now()
     # Count the occurrences of each crime type
    crimeCounts = data.groupby('Crm Cd Desc').size().sort_values(ascending=False)

    # Select the top 10 most frequent crime types
    topCrimeTypes = crimeCounts.head(10)

    # Print the results
    for i, (crimeType, count) in enumerate(topCrimeTypes.iteritems()):
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] {i+1}. {crimeType}: {count}")



def printLALunchTime(data):
    now = datetime.now()
    # Make a copy of the data so that the original data is not modified
    dataCopy = data.copy()
    dataCopy['DATE OCC'] = pd.to_datetime(dataCopy['Date Rptd'], format='%m/%d/%Y %I:%M:%S %p') - pd.to_datetime(dataCopy['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p')
    # Convert the Date Occurred column to a datetime datatype
    dataCopy['DATE OCC'] = pd.Timestamp('1900-01-01') + pd.to_timedelta(dataCopy['DATE OCC'], unit='D')

    # Extract the victim sex and time of the crime
    dataCopy['Vict Sex'] = dataCopy['Vict Sex'].str.upper()

    # Convert 'TIME OCC' column to string and remove any non-numeric characters
    dataCopy['TIME OCC'] = dataCopy['TIME OCC'].astype(str).str.replace(r'\D', '', regex=True)

    # Convert 'TIME OCC' column to datetime object
    dataCopy['TIME OCC'] = pd.to_datetime(dataCopy['TIME OCC'], format='%H%M', errors='coerce')

    # Remove any rows with missing datetime values
    dataCopy.dropna(subset=['TIME OCC'], inplace=True)

    # Extract hour component from datetime object
    dataCopy['TIME OCC'] = dataCopy['TIME OCC'].dt.hour

    # Filter the dataset to only include crimes between 11:00am and 1:00pm
    dataLunchTime = dataCopy[(dataCopy['TIME OCC'] >= 11) & (dataCopy['TIME OCC'] <= 13)]

    # Calculate the number of crimes for each gender
    numFemalVictims = len(dataLunchTime[dataLunchTime['Vict Sex'] == 'F'])
    numMaleVictims = len(dataLunchTime[dataLunchTime['Vict Sex'] == 'M'])

    # Print the results
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] Evidence:")
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] Number of female victims between 11:00am and 1:00pm: {numFemalVictims}")
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"[{current_time}] Number of male victims between 11:00am and 1:00pm: {numMaleVictims}")

    print(f"\n[{current_time}] Answer:")
    if numFemalVictims > numMaleVictims:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"\n[{current_time}] Women are more likely to be the victim of a crime during lunchtime.")
    elif numFemalVictims < numMaleVictims:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"\n[{current_time}] Men are more likely to be the victim of a crime during lunchtime.")
    else:
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"\n[{current_time}] There is an equal likelihood of men and women being the victim of a crime during lunchtime.")


def OlderManTop5(data):
    now = datetime.now()
    # Convert DATE OCC column to datetime format
    data["DATE OCC"] = pd.to_datetime(data["DATE OCC"], format="%m/%d/%Y %I:%M:%S %p")

    # Filter for crimes that occurred in December 2018 and involved a victim age 65 or older and male gender
    filteredData = data.loc[(data["DATE OCC"].dt.year == 2018) & (data["DATE OCC"].dt.month == 12) & (data["Vict Age"] >= 65) & (data["Vict Sex"] == "M"), :]

    # Count the number of crimes in each area and sort in descending order
    crimeCountByArea = filteredData["AREA NAME"].value_counts().sort_values(ascending=False)
    
    # Print the top 5 dangerous areas
    for i,(area, count) in enumerate(crimeCountByArea.head(5).items(), 1):
        current_time = now.strftime("%H:%M:%S.%f")
        print(f"[{current_time}] {i}. {area}: {count}")
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


def sortData(lst, format):
    ''' method for sorting data frame data by passed in column_name
        lst             Data list to sort
        format = 1      Ascending
        format = 2      Descending'''
    if (format == 1):
        heapSort(lst)
    elif (format == 2):
        minHeapSort(lst, len(lst))
        # lst.reverse()
    else:
        print("bad arg", format, "passed to sortData")

    # def sortData(dframe, column_name):
#     ''' method for sorting data frame data by passed in column_name'''
#     heapSort()


def minHeapify(lst, n, i):
    smallest = i    #initialize smallest as root
    l = 2 * i + 1 # left child
    r = 2 * i + 2 # right child

    #check left child is smaller
    if l < n and lst[l] < lst[smallest]:
        smallest = l
    
    # check if right child is smaller
    if r < n and lst[r] < lst[smallest]:
        smallest = r
    
    # swap if smallest is not root
    if smallest != i:
        (lst[i], lst[smallest]) = (lst[smallest], lst[i])
        # recursively minheapify the subtree
        minHeapify(lst, n, smallest)
    


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

def minHeapSort(lst, n):
    for i in range(int(n/2) -1, -1, -1):
        minHeapify(lst, n, i)
        
    for i in range(n-1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        minHeapify(lst, i, 0)

def describeColumn2(clean_sorted_lst, col_number, data_bools, **kwargs):
    # print("in describecolumn2")
       
    total = counts(clean_sorted_lst)
    unique = uniqueCounts(clean_sorted_lst)
    if (data_bools[col_number]["mean"] == True):
        # print("getting standev")
        mvs = stanDev(clean_sorted_lst)
    else:
        mvs = None
    if (data_bools[col_number]["median"] == True):
        # print("getting median")
        med = medianFunc2(clean_sorted_lst)
    else:
        med = None
    if (data_bools[col_number]["mode"] == True):
        # print("getting mode")
        mode = modeFunc2(clean_sorted_lst)
    else:
        mode = None
    if (data_bools[col_number]["min"] == True):
        # print("getting min")
        min = minFunc2(clean_sorted_lst)
    else:
        min = None
    if (data_bools[col_number]["max"] == True):
        # print("getting max")
        max = maxFunc2(clean_sorted_lst)
    else:
        max = None
        
   
    print("Count:", total)
    print("Unique:", unique)
    
    
    
        # if 'dframe' in kwargs:
    #     df = kwargs.get('dframe')
    #     print("made it here")
    #     df['days'] = pd.to_datetime(df[kwargs.get('cname')]).sub(pd.Timestamp('2010-01-01')).dt.days
    #     print(df['days'])
    #     clean_sorted_lst =     
    
    
    if 'dtype' in kwargs:
        # print("date passed in")
        
        
        d = pd.to_datetime("2010-01-01") + pd.DateOffset(days=mvs['mean'])
        print("Mean:", d.strftime("%m/%d/%Y"))
        
        d = pd.to_datetime("2010-01-01") + pd.DateOffset(days=med)
        print("Median:", d.strftime("%m/%d/%Y"))
        
        d = pd.to_datetime("2010-01-01") + pd.DateOffset(days=mode)
        print("Mode", d.strftime("%m/%d/%Y"))
        
        d = pd.to_datetime("2010-01-01") + pd.DateOffset(days=min)
        print("Minimum:", d.strftime("%m/%d/%Y"))
        
        d = pd.to_datetime("2010-01-01") + pd.DateOffset(days=max)
        print("Maximum:", d.strftime("%m/%d/%Y"))
        
        print("STDEV: ", mvs['st_dev'], "days")
        print("Variance: ", mvs['var'], "days squared")

    else:
        if (mvs is not None):
            print("Mean:", mvs['mean'])
        else:
            print("Mean: N/A")
        if (med is not None):
            print("Median:", med)
        else:
            print("Median: N/A")
        if (mode is not None):
            print("Mode", mode)
        else:
            print("Mode: N/A")
        if (min is not None):
            print("Minimum:", min)
        else:
            print("Minimum: N/A")
        if (max is not None):
            print("Maximum:", max)
        else:
            print("Maximum: N/A")
        if (mvs is not None):
            print("STDEV: ", mvs['st_dev'])
            print("Variance: ", mvs['var'])
        else:
            print ("STDEV: N/A")
            print ("Variance: N/A")
    
    


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
    print("25. Sort by Column:")
    print("26. Back to the Main Menu")
        

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
    
def printSortMenu(header_list):
    print("Sort Data Column:")
    print("**************************")
    for i in range(len(header_list)):
        print(f"[{i}] {header_list[i]}")   
    print("Select the column number to sort")
    print("Enter -1 to return to the previous menu")
    
def printAscDescMenu():
    print("Select Ascending or Descending")
    print("[1] Ascending")
    print("[2] Descending")
    
def printDataAnalysis(df):
    now = datetime.now()
    dataCopy = df.copy()
    
    print("Data Analysis:")
    print("***************")
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"[{current_time}] 1. Show the total unique count of crimes per year sorted in descending order:")
    totalUniqueCount(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 2. Show the top 5 areas with the most crime events in all years:")
    countCrimesByArea(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 3. Show all months and the unique total count of crimes sorted in increasing order.")
    MonthsUniqueCrimes(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 4. Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.")
    Top10Streets(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 5. Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.")
    Top5HWood(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 6. Print the details of the crime that that took the most time (in hours) to be reported.")
    MostTime(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 7. Show the 10 top most common crime types (Crm Cd Desc) overall across all years.")
    printMostCommonCrime(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 8. Are woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.")
    printLALunchTime(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 9. What is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.")
    printCCFrauds(dataCopy)
    
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"\n[{current_time}] 10. List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.")
    OlderManTop5(dataCopy)
    
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
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #2
                    dict(count=True, unique_count=True, mean=True, median=True, mode=True, stdev=True, var=True, min=True, max=True), #3
                    
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
            while (sub_menu_option != 26):
                # get user input until correct
                #os.system("clear")
                clear()
                if (print_msg != "" ):
                    print(print_msg)
                    print_msg = ""
                printDataExpMenu()
                sub_menu_option = getResponse(printDataExpMenu, 21, 26)
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
                    
                    print("cleaning data...")
                    clean_df = data_frame.dropna(axis = 'index', subset = [all_headers[col_number]])
                    
                    # clean out 0.0's from lat and long columns
                    if (all_headers[col_number] == 'LAT' or all_headers[col_number] == 'LON'):
                        clean_df = clean_df[clean_df[all_headers[col_number]] != 0]
                        
                    elif (all_headers[col_number] == 'Vict Age'):
                        clean_df = clean_df[clean_df[all_headers[col_number]] > 0]
                        clean_df = clean_df[clean_df[all_headers[col_number]] != 118]
                        # print("should have cleaned neg values from vic age")
                    
                    elif (all_headers[col_number] == 'Vict Sex'):
                        clean_df = clean_df[clean_df[all_headers[col_number]] != 'X']
                        clean_df = clean_df[clean_df[all_headers[col_number]] != 'N']
                        
                    elif (all_headers[col_number] == 'Vict Descent'):
                        clean_df = clean_df[clean_df[all_headers[col_number]] != '-']
                         
                    elif (all_headers[col_number] == 'Date Rptd' or all_headers[col_number] == 'DATE OCC'):
                        # clean_df = pd.to_datetime(clean_df[all_headers[col_number]], format='%m/%d/%Y %I:%M:%S %p')
                        clean_df[all_headers[col_number]] = pd.to_datetime(clean_df[all_headers[col_number]], format="%m/%d/%Y %I:%M:%S %p")
                        # print("made the clean df yo")
                        clean_df[all_headers[col_number]] = pd.to_datetime(clean_df[all_headers[col_number]]).sub(pd.Timestamp('2010-01-01')).dt.days
                        
                    
                    clean_lst = clean_df[all_headers[col_number]].to_list()
                    # print("made the clean list")
                    clean_sorted_lst = sorted(clean_lst)
                    # print("made the clean sorted list")
                    # fin = open("log.log", "w")
                    # for val in clean_lst:
                    #     # print(val)
                    #     fin.write(str(val) + '\n')
                    # fin.close()
                    
                    print("done cleaning data...")
                    
                    print(f"{all_headers[col_number]} stats:")
                    print("============================")
                    

                    try:
                        s_time = time.time()
                        
                        if (all_headers[col_number] == 'Date Rptd' or all_headers[col_number] == 'DATE OCC'):
                            describeColumn2(clean_sorted_lst, col_number, data_bools, dtype='date')
                        else:
                            describeColumn2(clean_sorted_lst, col_number, data_bools)
                            
                        # describeColumn(datalst, col_number, data_bools)
                        # describeColumn(clean_lst, col_number, data_bools)
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
                
                elif (sub_menu_option == 25):
                    clear()
                    printSortMenu(all_headers)
                    col_number = getResponse(printSortMenu, -1, len(all_headers)-1, arg_list=all_headers)
                    if (col_number == -1):
                        continue
                    printAscDescMenu()
                    sort_type = getResponse(printAscDescMenu, 1, 2)
                    
                    clean_df = data_frame.dropna(axis = 'index', subset = [all_headers[col_number]])
                    
                    if (all_headers[col_number] == 'DATE OCC' or all_headers[col_number] == 'Date Rptd'):
                        try:
                            clean_df[all_headers[col_number]] = pd.to_datetime(clean_df[all_headers[col_number]], format="%m/%d/%Y %I:%M:%S %p")
                        except:
                            print("couldn't format",all_headers[col_number],"as a date")
                            print("attempting to sort without converting...")
                    
                        # split the Mocodes
                    
                    clean_lst = clean_df[all_headers[col_number]].to_list()
                    
                    if (all_headers[col_number] == 'Mocodes'):
                        new_lst = list()
                        for codes in clean_lst:
                            try:
                                new_lst.append(int("".join(codes.split())))
                            except:
                                continue
                        # print(new_lst)                            
                        clean_lst = new_lst
                    
                    sortData(clean_lst, sort_type)
                    print(clean_lst)
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
            sub_menu_option = getResponse(printMenu, -1, 2)
            
            if sub_menu_option != -1:
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
