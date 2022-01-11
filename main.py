"""
Title:	        Sum of factorial's digits
Client:         Corigine
Author:	        Annemie Potgieter
Created:	    05-Jan-2022
Status:	        Completed
Description:    Finding the sum of the digits of a factorial (n!)
"""

# importing packages
import math
import numpy as np
import time
#import user_defined_func


# user defined functions
def sum_of_d_fct(d_fct):
    """
    Calculating the factorial of an integer and the sum of its digits
    :param d_fct: user input number which is an integer
    :return: sum of the digits of d_fct!
    """
    # Calculating factorial
    fctril = math.factorial(d_fct)
    #len_fctril = np.ceil(math.log10(fctril))  # useful when debugging
    print(str(d_fct) + "! is: \n" + str(fctril))

    # Calculating sum of digits
    d_ans = 0
    while fctril >= 1:  # for every digit in the factorial
        d_indv = fctril % 10  # individual digit from the modulus of the number
        d_ans = d_ans + d_indv  # adding the value of the individual digit
        fctril = fctril // 10  # move one digit to the left

    return int(d_ans)


def sum_of_f_fct(f_fct):
    """
    Calculating the factorial of a float and the sum of its digits
    :param f_fct: user input number which contains decimals
    :return: sum of the digits of f_fct!
    """
    # Calculating factorial
    fctril = math.gamma(f_fct + 1)
    print(str(f_fct) + "! is: \n" + str(fctril))
    print("Note that all decimal numbers may not be shown.")

    # Calculating sum of digits
    d_ans = 0
    int_fctril = np.floor(fctril)
    while int_fctril >= 1:  # for every integer in the factorial
        d_indv = int_fctril % 10  # individual digit from the modulus of the number
        d_ans = d_ans + d_indv  # adding the value of the individual digit
        int_fctril = np.floor(int_fctril / 10)  # move one digit to the left
    while fctril > 0:  # for every decimal digit in the factorial
        f_indv = np.floor(10 * (fctril % 1))
        d_ans = d_ans + f_indv
        fctril = (fctril * 10) % 1  # move one digit to the right

    return int(d_ans)


def cond(num):
    """
    Checking if number is input and if it is positive.
    :param num: user input number
    :return:
    """
    if (num.strip('-')).isdecimal():
        if float(num) < 0:
            print("Number should be positive.\n")
            return False
        else:
            return True
    elif "." in num:
        if float(num) < 0:
            print("Number should be positive.\n")
            return False
        else:
            return True
    else:
        print("Input must be a number.\n")
        return False

# Initiating variables:
ans = "Error"
conti = False
user_num = ""
i = 0

# Receiving user input and checking conditions
while conti == False:
    user_num = input("Enter a number:\n")
    conti = cond(user_num)
    i += 1
    if i > 20:
        print("Too many errors. Exiting.")
        time.sleep(1)
        exit()

# Convert input to relevant variable and calculate factorial
if (user_num.strip('-')).isdecimal():
    if float(user_num) > 100000:
        yn = input("Refrain from choosing large numbers. Would you like to continue? (Yes or No)")
        if yn == "No":
            exit()
        elif yn != "Yes":
            print("Invalid input. Exiting.")
            time.sleep(1)
            exit()
    user_num = int(user_num)
    ans = sum_of_d_fct(user_num)
elif "." in user_num:
    while float(user_num) > 170.624:  # Checking restrictions:
        user_num = input("Please enter a smaller number:\n")
    user_num = float(user_num)
    ans = sum_of_f_fct(user_num)
else:
    print("Input is not a valid number.")
    exit()

# Final message to user
print("\nThe sum of the digits of " + str(user_num) + "! is: \n" + str(ans))
