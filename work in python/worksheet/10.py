# # """
# # matrix multiplication 


# # """
# x = [ 
#  [2,3,4],
#  [3,4,5],
#  [6,7,8]
# ]
# row = len(x)
# colm = len(x[0])
# # for i in range(0 , row):
# #     for j in range(0, colm):
# #         print(x[i][j], end=" ")
# #     print()



# """ this the code to trranspose a matrix
# # result = [[0]*row for _ in range(colm ) ] 
# # # r = len(result)
# # # c = len(result[0])
# # for i in range(row):
# #     for j in range (colm):
# #         result[j][i] = x[i][j]
# # print(result)

# """



# result  = [[0]*row for _ in range(colm ) ]
# # for i in range (0 , row):
# #     for j in range(0 , colm):
# #         result[j][i] = x[i][j]
# # print(result)

# for i in range(0, row):
#     for j in range(0, colm):
#         result[i][colm - 1 - j] = x[i][j]
# print(result)

# n = 10 
# for i in range(2,10):
#     if (n % i)  == 0:
    
#         print(i , end  =" " )


n = 50
for num in range(2,n + 1):
    for j in range(2, num):
        if (num % j) == 0 :
            break
    else:
        print(num, end =" ")
 
# n = 50

# for num in range(2, n + 1):
    
#     for i in range(2, num):
#         if (num % i) == 0:
#             break  
#     else:
#         print(num, end=" ")
