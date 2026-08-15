"""
print fibonacci series until user say 

"""
x = int(input("enter the no of terms: "))

a, b = 0, 1 
for i in range(x):
    print(a)
    a,b = b, b+a

