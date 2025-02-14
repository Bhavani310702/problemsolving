# start = int(input("Enter a first number"))
# end = int(input("Enter a second number"))

# for i in range(start, end + 1):
#     temp = i
#     power = len(str(i))
#     sum_of_digits = 0

#     for j in str(i):
#         sum_of_digits += int(j) ** power

#     if i == sum_of_digits:
#         print(i)


# start = int(input("Enter a first number"))
# end = int(input("Enter a second number"))

# for i in range(start, end + 1):
#     count = 0

#     for j in range(1, i):  
#         if i % j == 0:
#             count += j

#     if count == i:
#         print(i)


#  leap year---------------------------

# year=int(input("Enter a year"))
# while True:
#     year += 1
#     if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("leap year")
#         break
#     else:
#         print("not a leap year")




# amstrong---------------------

# lower_range = 100
# upper_range = 10000

# for i in range(lower_range, upper_range + 1):
#     temp = i
#     power = len(str(i))
#     sum = 0
#     while temp > 0:
#         rem = temp % 10
#         sum += rem ** power
#         temp = temp // 10
#     if i == sum:
#         print(i)

# ----------------------------------------------------

# lower_range = 100
# upper_range = 10000

# for i in range(lower_range, upper_range + 1):
#     temp = i
#     sum = 0
#     while temp > 0:
#         rem = temp % 10
#         sum += rem ** 3
#         temp = temp // 10
#     if i == sum:
#         print(i)


# num = int(input("enter a number"))
# temp = num
# sum = 0
# while temp > 0:
#     rem = temp % 10
#     print(rem)
#     sum +=rem ** 3
#     temp = temp // 10
# print("Amstrong") if sum == num else print("not a Amstrong") 




#positive and negative numbers  ***************

# num=int(input("enter a number"))
# if num>0:
#    print("positive")
# elif num<0:
#     print("negative") 
# else:
#     print("zero")     


# even and odd numbers**********************

# num=int(input("enter the number"))
# if num %2 == 0:
#     print("even")
# else:
#     print("odd")  

# eligible vote for age >=18*******************

# age=int(input("enter the number")) 
# if age >= 18:
#     print("eligible for vote")
# elif age < 18:
#     print("miners")  
# else:
#     print("go to school")    

# greatest of two numbers******************

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a > b:
#     print("The greatest number is {a}")
# else:
#     print("The greatest number is {b}")

# students scores more than 40 pass****************

# num=int(input("enter the number"))
# if num > 40:
#     print("pass")
# else:
#     print("fail")

# day of the week based on the number**************

# num=int(input("enter the number"))
# if num == 1:
#     print("monday")
# elif num == 2:
#     print("Tuesday") 
# elif num == 3:
#     print("Wednesday") 
# elif num == 4:
#     print("Thursday") 
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday") 
# elif num == 7:
#       print("Sunday")
# else:
#       print("error")

# simple calculator using operators****************

# opt=input("enter to perform").lower()
# opd=float(input("enter first number"))
# opd1=float(input("enter second number"))
# if opt == 'add':
#     print(opd+opd1)
# elif opt == 'sub':
#     print(opd-opd1)
# elif opt == 'mul' :
#     print(opd*opd1) 
# elif opt == 'div' :
#     str="division by zero not possible"  if opd1 == 0 else opd/opd1 
#     print(str) 
# else:
#     print("inavalid error")

# name of the month based on the number*************

# num=int(input("enter the number"))
# if num == 1:
#     print("January")
# elif num == 2:
#     print("Febraury") 
# elif num == 3:
#     print("March") 
# elif num == 4:
#     print("April") 
# elif num == 5:
#     print("May")
# elif num == 6:
#     print("June") 
# elif num == 7:
#     print("July")
# elif num == 8:
#     print("Agust") 
# elif num == 9:
#     print("September")
# elif num == 10:
#     print("October") 
# elif num == 11:
#     print("November")
# elif num == 12:
#     print("December")
# else:
#     print("Not found")

# MEDIUM QUESTIONS-------------------------------------------------------------

# greatest of three numbers*****************

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# if a > b and b > c:
#     print("a is greater")
# elif b > c:
#     print("b is greater")
# else:
#     print("c is greater")

# check a leap year************************

year = int(input("Enter a year "))
while True:
    year+=1
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("year is a leap year.")
        break
    else:
        print("year is not a leap year.")

# year=int(input("enter anumber"))
# str='leap year' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 'not a leap year'
# print(str)

# calculate the grade of a student*************************

# num=int(input("enter the number"))
# if num >= 90:
#     print("A grade")
# elif num >=80:
#     print("b grade") 
# elif num >= 70:
#     print("c grade")
# else:
#      print("fail")   

# Three sides of triangle***************************

# side=int(input("enter a number"))
# side1=int(input("enter a number"))
# side2=int(input("enter a number"))
# print('triangle possible' if (side+side1 > side2) and (side2+side >side1) and (side1+side2 >side) else 'not a triangle')

# side,side1,side2=map(float,input("enter a number").split(','))
# print('triangle possible' if (side+side1 > side2) and (side2+side >side1) and (side1+side2 >side) else 'not a triangle')


# write a program to classify entered by the users as a  voewl,constant and neither****************************

# str=input("enter a one character").lower()

# if str in ['a','e','i','o','u']:
#     print("vowels")
# else:
#     print("constant")   

# if str in 'aeiou':
#      print("vowels")
# else: 
#     print("constant") 

# if len(str) > 1 or len (str) == 0:
#      print("i am not run the code") 
# else:
#      if str in 'aeiou':
#           print("vowels")
#      elif str.isalpha():      
#           print("constant")
#      else:
#           print("neither") 

# 

# health=int(input("enter a number"))
# health1=int(input("enter a number"))
# attack=int(input("enter a number"))
# attack1=int(input("enter a number"))
# if attack > attack1:
#     print("warriors 1 wins")
# elif attack1 > attack:
#     print("warriors 2 wins")
# else:
#     if health > health1:
#         print("warriors 1 wins") 
#     elif health1 > health:
#         print("warriors 2 win") 
#     else:
#         print("draw") 


# Name="ramya"  
# password="ammu"

# username=input("enter a name")
# password_name=input("enter a password")

# if username == Name and password_name == password:
#     print("login successfully")
# else:
#     ("login failed u r not user")


# LOOPS----------------------------

# print 1 to 100 using for loop**************

# for i in range(1,101):
#     print(i)



# print the sum of the first n natural numbers************

# num = int(input("Enter the number"))
# sum = 0
# for i in range(1,20):  
#      sum += i
# print(sum)         # this will returns the only 19 sum of the natural numbers

# n = int(input("Enter the number"))
# print((n * (n + 1)) // 2 )     # This will returns the summ of  the 20 nutural numbers


# print 1 to 50 even numbers***************

# for i in range(1,50):
#     if  i %2 == 0:
#         print(i,"even")

# i = 0
# while i <= 50:
#     print(i)
#     i += 2

# for i in range(0,52,2):
#     print(i)

# reverse number and sum the num*************

# num = int(input("Enter a number: "))
# reverse = 0
# sum = 0
# while num > 0:
#     digit = num % 10           
#     reverse = (reverse * 10) + digit  
#     sum += digit       
#     num //= 10                 
# print(reverse)
# print(sum)

#  febnoccai values print first 20********************************

# def feb(n):
#     if n<=1:
#         return n
#     return feb(n-1)+feb(n-2) 
# print(feb(20))     

# def fibonacci(n):
#     a, b = 0, 1 
#     for _ in range(n):
#         print(a)  
#         a, b = b, a + b    
# num = 10
# fibonacci(num)

# Write a program to display the multiplication table of a given**************
# number. First 20

# for i in range(1,21):
#    print(3,'x',i,'=', i*3)

# for i in range(0,21,3) :
#    print(3,'x',i//3,'=',i) 

# for i in range(0,20):
#     for j in range(0,20):
#         print(i,j)

# negative numbers  ---------------------------------

# num=0
# while num <= 0:
#         num=int(input("enter a number"))
#         print(num)

# Print all numbers from 1 to 100 that are divisible by 3 and 5
# using a for loop.


# for i in range(1,100):
#         if i % 3 == 0 and i % 5 == 0:
#               print(i)
          
# i. Write a program to calculate the factorial of a number using
# a while loop

# num = int(input("Enter a number: "))
# factorial = 1
# i = num
# while i > 0:
#     factorial *= i
#     i -= 1
# print(factorial)


# . Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits


# num=int(input("enter a number"))
# reverse=0
# sum = 0
# while num > 0:
#     rem= num % 10
#     reverse = (reverse * 10) + rem
#     num = num //  10
#     sum += rem
# print(reverse) 
# print(sum)  

# Write a program to count the number of digits in a given
# number using a while loop. and palindrome

# num=int(input("enter a number"))
# tem = num
# reverse=0
# sum = 0
# count = 0
# while num > 0:
#     rem= num % 10
#     reverse = (reverse * 10) + rem
#     num = num //  10
#     sum += rem
#     count += 1
# print(reverse) 
# print(sum) 
# print(count)
# if tem == reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")  

# Implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit



# num = input("enter a number")
# while True:
#     if num == 'square':
#       username= float(input("enter a number"))
#       print( username ** 2)
#     elif num == 'cube':
#       username= float(input("enter a number")) 
#       print( username ** 3)
#     elif num == 'exit':
#       break
#     else:#ddde
#       print("inavalid input")


# i. Implement a basic login system where the user has three
# attempts to enter the correct password using a loop.

# user_account='Ramya'
# user_password='Ammu'
# allowed_attempt = 3
# while allowed_attempt > 0:
#     print("enter usrename and password")
#     print("you have",allowed_attempt,"attempts")

#     username = input("enter a username")
#     password = input("enter a password")

#     if user_account ==  username and  user_password == password:
#         print("login successfully")
#         break
#     else:
#         print("wrong password")
#         allowed_attempt -= 1


#   prime numbers-------------------------------------

# num = int (input("enter a number"))
# count = 0
# for i in range(1, num + 1):
#    if num % i == 0:
#      count += 1
# if count == 2:
#   print ("it is a prime")
# else:
#   print("not a prime number") 
 
# ----------------------------------------------------------------------

# num =int(input("enter a number"))
# flag=True
# if num == 0:
#     print("it is prime")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             flag= False
#             break
# print("is is a prime") if flag == True else print("not a prime")     # this is a terinary operators 

# -----------------------------------------------------------------------

# def is_prime(num):
#     if num == 2:
#         return False
#     if num == 1:
#         return True
#     flag = True
# for i in range(2,int((num)/2) + 1:)
#     for i in range(2,int(num ** 0.5) + 1):
#         if num % i == 0:
#             flag  = False
#             break
#     res ="its a prime number" if flag == True else print("not a prime")
#     return res
# print( is_prime(17)) 

# comparision between time o(1) < o(root of n) < o(n) < o( n square) in time camplicity
   
#  list of prime numbers********************************

# numbers = [10, 15, 3, 7, 19, 25, 29, 33]
# primes = []
# for i in numbers:
#     if i > 1: 
#         is_prime = True
#         for i in range(2, i):
#             if i % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(i)
# print(primes)


#   any two numbers middle of the prime numbers************************

# start=int(input("enter a start number"))
# End=int(input("enter a end number"))
# for i in range(start,End + 1):
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)


# start=int(input("enter a start number"))
# End=int(input("enter a end number"))
# for i in range(start,End + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i) 

# num=int(input("enter a start number"))
# while True:
#     if num in [0,1,2]:
#         print("exit")
#         break
#     num-= 1
#     count = 0
#     for j in range(1, num+ 1):
#         if num % j == 0:
#             count += 1
#     if count == 2:
#         print(num)
#         break 


# num=int(input("enter a start number"))
# while True:
#     num+=1
#     count = 0
#     for j in range(1, num+ 1):
#         if num % j == 0:
#             count += 1
#     if count == 2:
#         print(num)
#         break 

# functions problems-----------------------------

# def even_odd (x):
#     if x % 2== 0:
#         print("even")
#     else:
#         print("odd")
# even_odd (12)   


# def prime(n):
#     if n <= 1:
#         return False
#     for i in range (2, n):
#         if n % i == 0:
#             return False
#     return True
# print(prime(11))


# def Amstrong(num):
#     temp = num
#     res = 0
#     while temp > 0:
#         rem = temp % 10
#         res += rem ** len(str(num)) 
#         temp = temp // 10
#     return res == num      
# print(Amstrong(153))
# -------------------------------------------------------
# def Armstrong(num,num1):
#     for i in range(num,num1 + 1):
#         temp = i
#         sum = 0
#         while temp > 0:
#             rem = temp % 10
#             sum += rem ** len(str(i))
#             temp = temp // 10
#         if i == sum:
#             print(i)
# Armstrong(100,10000)  
# -------------------------------------------------

        
           
  









