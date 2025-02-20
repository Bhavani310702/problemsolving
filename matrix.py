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
