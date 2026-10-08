#  x pattern 
x = int(input("Enter a number: "))
for i in range(x):
    for j in range(x):
        if i == j or i + j == x - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# # sand clock pattern
# x = int(input("Enter a number: "))
# for i in range(x):
#     for j in range(x):
#         if i == 0 or i == x - 1 or i == j or i + j == x - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()