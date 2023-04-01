import os

import files

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
        menu_list = files.getCsvFileList()
        printDataSelectMenu(menu_list)
        sub_menu_option = getResponse(printDataSelectMenu, len(menu_list), 1)
        print("calling readFile on",menu_list[sub_menu_option-1])
        
        

        
        
    


if __name__ == '__main__':
    os.system('clear')
    main()
