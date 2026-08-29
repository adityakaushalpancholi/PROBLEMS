""" 
so  there is a problem in which we have to find the sum of the string which is given in the input.
and then covert the sum into single digit 
"""
 
# so there is this first code 

x = int(input("enter a number "))
sum = 0
while x != 0:
    v = x % 10
    x = x // 10
    sum += v
    while sum > 9:
        z = sum%10
        sum = sum//10
        sum += z

      

print("Sum of digits:", sum)

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

