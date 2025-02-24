# Mul and division using recursion

# def multiple(a,b):
#     if b == 0:
#         return 0
#     if b > 0:
#       return a + multiple (a , b - 1)
#     else:
#        return multiple(a, -b)
# print(multiple(3,4))

# def division(a,b):
#    if a == 0:
#       return 0
#    if a < b:
#       return 0
#    return 1 + division(a - b, b)
# print(division(10, 2))

# Printing 1 to n numbers without multiple print statements and loops

# def natural_number(num,num1 =1):
#     if num1 > num:
#         return 
#     print(num1, end = " ")
#     natural_number(num,num1 + 1)
# natural_number(10)

# Sum of first n natural numbers using recursion

# def natural_numbers_sum(num):
#     sum = 0
#     for i in range(1,num + 1):
#         sum += i
#     return sum
# print(natural_numbers_sum(10))

# def natural_numbers_sum(n):
#      if n == 0:  
#         return 0
#      return n + natural_numbers_sum(n - 1)
# print(natural_numbers_sum(10))

# Printing a list in reverse order using recursion

# def print_reverse(lst, index=None):
#     if index is None:
#         index = len(lst) - 1  
#     if index < 0:  
#         return
#     print(lst[index], end=" ") 
#     print_reverse(lst, index - 1)  
# my_list = [1, 2, 3, 4, 5]
# print_reverse(my_list)




