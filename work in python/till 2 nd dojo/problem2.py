"""
i want to create a function that takes user input then
for units 1 to 100 it charges 1 
for 100 to 200 it charges 2
for 200 to 300 it charges 3
and for remaining units it charges 3  
"""
""" it is such a easy problem 
but it is my first encounter with such thing so the code is 
"""
x = int(input("enter the no of units: "))

if x <= 100:
    print("your bill is: ", x * 1)
elif x <= 200:
    print("your bill is: ", 100 * 1 + (x - 100) * 2)
elif x <= 300:
    print("your bill is: ", 100 * 1 + 100 * 2 + (x - 200) * 3)
else:
    print("your bill is: ", 100 * 1 + 100 * 2 + 100 * 3 + (x - 300) * 3)





