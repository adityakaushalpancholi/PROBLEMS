"""
ARMSTRONG NUMBER :

Such type of numbers whose sum of cubes of each digit is equal to the number itself. e.g. 153 --> (1)^3 + (5)^3 + (3)^3 = 1 + 125 + 27 = 153

Structure of Problem :

Take the input from the user.
Divide the digits in individual numbers.
Raise each number to the lenght of that no  and find the sum of them.
If sum == input, then the number Armstrong Number
"""
x = input("Enter a no: ")
sum = 0
n = len(x)
for char in x : 
    v = int(char)**n
    sum += v 
if sum == int(x): 
    print(" x is armstrong number ") 
else : 
    print( " You idiot ")
  