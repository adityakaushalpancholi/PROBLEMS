""" 
so  there is a problem in which we have to find the sum of the string which is given in the input.
and then covert the sum into single digit 
"""
 
# so there is this first code 

x = int(input("enter a number "))
sum = 0
while sum < 10 :
    v = x%10
    sum +=int(v)
    x = x//10
    if sum < 10 :
        print(sum)

    

"""
x = int(input())
total_sum = 0

while x > 0:
    total_sum += x % 10
    x = x // 10
    if x < 10 : 
        total_sum += x
        print(total_sum)
"""

