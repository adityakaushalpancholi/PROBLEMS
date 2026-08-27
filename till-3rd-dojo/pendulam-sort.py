"""
Input Format: 10
Output Format: [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]

"""

x = int(input("Enter a number: "))
evenList = []
oddList = []
pendulumSolution = []

for i in range(1, x+1):
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
    
oddList.reverse()
pendulumSolution = evenList + oddList
print(pendulumSolution)
