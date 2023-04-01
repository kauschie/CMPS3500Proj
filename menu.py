import os

def get_response(foo, max_val, min_val=1):
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
            
def print_base_menu():
    print("Main Menu:")
    print("**********")
    print("1. Load Data")
    print("2. Explore Data")
    print("3. Data Analysis")
    print("4. Print Data Set")
    print("5. Quit")
    
    
def main():
    print_base_menu()
    menu_option = get_response(print_base_menu, 5, 1)
    print("you selected option", menu_option)


if __name__ == '__main__':
    os.system('clear')
    main()
