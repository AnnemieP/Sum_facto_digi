# How ***sum_factorial_digits*** works and how to use it:  

This has been written with the intent of describing  

 - what this program does,  
 - how to get started,  
 - what options the user has and  
 - how the program works.  

## Purpose of program:  
***sum_factorial_digits*** was created to calculate the sum of any number's factorial’s digits. Learn more about factorials [here](https://en.wikipedia.org/wiki/Factorial).  

#### For example:  
The given number:        4  
​The factorial:           4! = 4x3x2x1 = 24  
The sum of the digits:   2+4 = 6  


#### Another example:  
The given number:        12  
The factorial:           12! = 12x11x10...3x2x1 = 479001600  
​The sum of the digits:   4+7+9+1+6 = 27  

## Getting started:
The easiest way to run this program is to open Docker play on a browser (when connected to the internet) by using the link [Docker play](https://labs.play-with-docker.com/), or googling Docker play.
Start your session by adding a new instance as seen on the left  
> \+ ADD NEW INSTANCE  

Enter the command:  
> $ docker run -ti annemiep/sum_factorial_digits  

Press enter. The program will ask you to enter a number which you can type in and press enter and voila, there you have the sum of the factorial's digits of the number you entered.

## User options:  
- You may enter any whole number or decimal number.  
- The largest decimal number that you may enter is 170.624  
- Whole numbers larger than 100 000 take very long to calculate and it is suggested that only smaller numbers are chosen.  
- Negative numbers (below 0) are not permitted as they do not have a factorial.  
- After entering an invalid number or symbol, the program will give you another try, but after too many wrong tries (>20), the program will exit.  

## How the code works:  
Imported packages are  
- math  
- numpy as np  
- time  

The program asks for a number input from the user and continues to do so while the input is not valid. The code also checks if a wrong input was given more than 20 times, and if so, it exits.  

The program converts the sting input to an integer if it is a whole number and to a float if it is a decimal. It also checks if the whole number is more than 100 000 as the program takes very long to calculate after 100 000. It also checks if the decimal more than 170.624 as this is the math operator's limit. The factorial of the whole numbers are calculated with  
> math.factorial(num)  

The factorial of the decimal numbers are calculated with  
> math.gamma(f_fct + 1)  

The factorial is displayed for the user.  

The sum of whole number digits is calculated by deviding the number by 10 and adding the remainder thereof (the rightmost digit) to the answer. The next digit is prepared by using the current shorterned number (devided by 10). All the digits are added to the answer untill the number is shortened to one digit.  

The sum of decimal digits is calculated looking at only the numbers after the decimal point by using the modulus of 1. The leftmost digit is added to the answer by multiplying the number by 10 and only adding that one digit which is on the left side of the decimal opint now. The next digit is prepared by using the current shorterned number (multiplied by 10). All the digits are added to the answer untill the number is shortened to zero.  

If a factorial number consists of both whole and decimal numbers, the sum is calculated seperately and the two answers added together.  

## Get this code:  
This code was written in Python 3.
> https://github.com/AnnemieP/Sum_facto_dig




