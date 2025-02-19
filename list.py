# 17) Finding the frequency of elements in an array.
# arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2 

# arr = [10, 30, 10, 20, 10, 20, 30, 10]
# unique_elements = set()
# for i in arr:
#     if i not in unique_elements:
#         unique_elements.add(i)
# for j in unique_elements:
#     count = 0
#     for i in arr:
#         if i == j:
#             count += 1
#     print(j,"=>", count)


# Print arr2 is subset or not subset of arr1
# let arr1=[2,21,5,7,3,5,7,3,1,6,14,44];
# let arr2=[7,3,1];--------------

# arr1 = [2, 21, 5, 7, 3, 5, 7, 3, 1, 6, 14, 44]
# arr2 = [7, 3, 1]
# subset = True
# for i in arr2:
#     if i not in arr1:
#         subset = False
#         break
# if subset:
#     print("arr2 is subset of arr1")
# else:
#     print("arr2 is not subset of arr1")

# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7.5.15]
# output: arr1 is subset of arr2-------------


# arr1 = [1,3,4,5,2]
# arr2 = [2,4,3,1,7.5,15]
# subset = True
# for i in arr2:
#     if i not in arr1:
#         subset = False
#         break
# if subset:
#     print("arr1 is  subset of arr2")
# else:
#     print("arr1 is not subset of arr2")


# 20) Wap to print the number of pairs formed by the array of elements
#  Input: 10 20 10 30 20 20	  Output: 2 pairs
# #  Input: 30 50 30 50 20 50 50 20 50 50    Output : 5 pairs

# def pair(arr):
#     count = {}
#     pair = 0
#     for i in arr:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     for j in count.values():
#         pair += j // 2
#     return pair  
# arr = [10,20, 10, 30, 20, 20] 
# arr1 = [30, 50, 30, 50, 20, 50, 50, 20, 50, 50]    
# print(pair(arr),"pairs")
# print(pair(arr1),"pairs")  

