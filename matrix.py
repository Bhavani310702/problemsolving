# 3)read a matrix 
# input : 
# 2 3 4 
# 3 9 2 
# 3 4 1 
# find the sum of numbers 2+9+1+4+3=?

# matrix = [
#     [2, 3, 4],
#     [3, 9, 2],
#     [3, 4, 1]
# ]
# target_numbers = {2, 9, 1, 4, 3} 
# total_sum = 0
# for i in matrix:
#     for num in i:
#         if num in target_numbers:
#             total_sum += num
# print(total_sum)

# matrix = [
#     [2, 3, 4],
#     [3, 9, 2],
#     [3, 4, 1]
# ]
# sum_diagonals = [2,9,1,4,3]
# total_sum = sum(sum_diagonals)
# print(total_sum)


# 2) read a matrix 
# input : 
# 2 3 4 
# 3 9 2 
# 3 4 1 
# find the sum of outer layers 
# 2+3+4+3+3+3+4+1+2= ?

# list = [[2,3,4],[3,9,2],[3,4,1]]
# sum = 0
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         if i == 0 or j == 0 or i == len(list) -1 or j == len(list[i]) - 1:
#              sum +=list[i][j]
# print(sum)


# 4) print the outer number in a matrix
# input: 
# 1 2  3
# 5  4  1
# 3  6  1
# Out:
# 1 2 3 
# 5    1
# 3 6 1

# list = [[1,2,3],[5,4,1],[3,6,1]]

# for i in range(len(list)):
#     for j in range(len(list[i])):
#          if i == 0 or j == 0 or i == len(list) - 1 or j == len(list) - 1:
#            print(list[i][j], end = " ")
#          else:
#              print(" ",end = " ")
#     print()  





# 5) 1 2 3
#     4 5 3
#     2 5 3
# Print the outer layer elements side by side
# Outer layer elements: 1 2 3 4 3 2 5 3

# ismatrix = [[1,2,3],[4,5,3],[2,5,3]]
# sum = []
# for i in range(len(ismatrix)):
#     for j in range(len(ismatrix[i])):
#         if i == 0 or i == len(ismatrix)-1:
#           sum.append(ismatrix[i][j])
#         else:
#           if j == 0 or j == len(ismatrix)-1:
#                sum.append(ismatrix[i][j])
# print(sum)

# 5) 1 2 3
#     4 5 3
#     2 5 3


# Output: print the diagonal elements side by side:
# Diagonal elements are :1 5 3 3 5 2

 
# list =[[1,2,3],[4,5,3],[2,5,3]]
# sum = []
# for i in range(len(list)):
#    for j in range(len(list[i])):
#       if i == j or i + j == len(list) - 1:
#          sum.append(list[i][j])
#          if i == j and i  + j == len(list) - 1:
#              sum.append(list[i][j])
# print(sum)