"""
input: 5 


output: 


Hint: Use an outer loop for each row (1 to n) and an 
inner loop that runs from 1 up to the current row number.
"""
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


