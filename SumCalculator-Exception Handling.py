#Favian Mokaya Imbera SCT211-0022/2021

#Enter name, number1 and number2 respectively

def get_name():
    return input()
#This function takes no arguments and simply returns the name entered by the user.

def get_num():
    while True:
        try:
            return int(input())
#If the user enters a non-numeric value, a ValueError will be raised
        except ValueError:
            print("Sorry, I didn't understand that. Please enter a number.")
#This except block will catch the error, display an error message, and then loop back to the beginning

#The function above takes a string 'prompt' as 

def main():
    name = get_name()
    num1 = get_num()
    num2 = get_num()

    sum = num1 + num2
    print("Hello, " + name + ". The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))

if __name__ == "__main__":
    main()