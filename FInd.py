# Assignment 12 
# Program to find out the sum of the first n natural numbers :
# n = int(input("Enter the limit till which sum is to be calculated :"))
# s=0
# for i in range (1,n+1):
#     s+=i
# print("Sum of first",n,"Natural Numbers = ",s)
# Assignment 13
# Program to find factorial of a number
# n = int(input("Enter the no. till which factorial is to be calculated :"))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print("factorial of ",n,":",fact)
# Assignment 14 :
# # Program to check prime number or composite number 
# n = int(input("Enter a number : "))
# count = 0
# i = 1
# while(i<=n):
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print(n,"is a Prime Number")
# elif(count==1):
#     print(n,"is a Special Number")
# else:
#     print(n,"is a composite number")
       

# # Assignment 15 :
# # Program to print all the Prime Numbers within a given range 
# lw = int(input("Enter the lower limit : "))
# uw = int(input("Enter the upper limit : "))
# for n in range (lw,uw+1):
#     if(n>1):
#         for i in range(2,int(n**0.5)+1):
#             if(n%i)==0:
#                 break
#         else:
#             print(n)

# # Assignment 16 :
## Program to print all the factors of a given number
# num=int(input("Enter a number : "))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)

# # Assignment 17 :
# Program to check if a given number is a perfect number or not
# num = int(input("Enter a number :"))
# s = 0
# for i in range (1,num):
#     if(num%i == 0):
#         s+=i
# if(s==num):
#     print(num,"is a Perfect Number")
# else:
#     print(num,"is not a Perfect Number")


# num = int(input("Enter a number : "))
# s= 0
# for i in range(1,num):
#     if(num%i==0):
#         s+=i
# if(s==num):
#     print(num,"is a perfect number .")
# else:
#     print(num,"is not a perfect number.")


# # Assignment : 18
# # Write a program in python to print the sum of the following series : S = 1+4+9+....+n
# n = int(input("Enter the limit : "))
# s = 0
# for i in range (1,n+1):
#     s+=i*i
# print("sum of series =",s)
# Assignment 19 :
# Write a program in pyhton to print the sum of the following series: S = 1-2+3-4+5-6+....+N
# n = int(input("Enter the limit : "))
# s = 0
# for i in range (1,n+1):
#     if(i%2 == 0):
#         s-=1
#     else :
#         s+=i
# print("Sum of series = ",s)
# # Assignment 20 :
# # Palindrome number
# num = int(input("Enter a number :"))
# flag = num
# rev = 0
# while(flag > 0):
#     q = flag%10
#     flag=flag//10
#     rev=(rev*10)+q
# if(num==rev):
#     print(num,"is a palindrome number ")
# else:
#     print(num,'is not a palindrome number ')
# # Assignment 21:
# # Palindrome Number within a given range 
# lw = int(input("Enter the lower limit :"))
# uw = int(input("Enter the upper limit :"))
# print("Palindrome Numbers from",lw,"to",uw,"are = ")
# for i in range (lw,uw+1):
#     rev = 0
#     temp = i
#     while(temp>0):
#         r=temp%10
#         rev=(rev*10)+r
#         temp=temp//10
#     if(i==rev):
#         print(rev)
# # Assignment 22:
# # # Armstrong Number
# num = int(input("Enter a number :"))
# temp = num
# s=0
# while(temp>0):
#     q=temp%10
#     cb=q*q*q
#     s+=cb
#     temp=temp//10
# if(num==s):
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")
# # Assignment 23
# # Armstrong Number within a given range
# lw = int(input("Enter the lower limit :"))
# uw = int(input("Enter the upper limit :"))
# print("Armstrong Numbers from",lw,"to",uw,"are = ")
# for i in range(lw,uw+1):
#     temp = i
#     s = 0
#     while(temp>0):
#         q = temp%10
#         cb = q*q*q
#         s+=cb
#         temp=temp//10
#     if(i==s):
#         print(s)
# # Assignment 24
# # Factorial of a Number
# n = int(input("Enter the no. till which factorials is to be calculated :"))
# fact = 1
# for i in range (1,n+1):
#     fact*=i
# print("Factorial of",n,":",fact)
# class Details:
#     name = "Ranjan"
#     age = 20

# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# import calendar
# yy = 2024

# print(calendar.calendar(yy))

# import asyncio
# async def fn():
# 	print('This is ')
# 	await asyncio.sleep(0) # time taking to print the next statement
# 	print('asynchronous programming')
# 	await asyncio.sleep(0)
# 	print('and not multi-threading')
# asyncio.run(fn())


# import calendar
# yy = 2024
# mm = 3
# print(calendar.month(yy,mm))


#Concept of local variale and global variable

# icecream = "Vanilla"    #global variable
# def foods():
#     vegetable = "Potato"    #local variable
#     fruit = "Lichi"         #local variable
#     print(vegetable + " is a local variable value.")

# foods()
# print(icecream + " is a global variable value.")
# print(fruit + " is a local variable value.") 

# Converting string to bytes
# str1 = "This is a string"
# arr1 = bytes(str1, 'utf-8')
# print(arr1)
# arr2 = bytes(str1, 'utf-16')
# print(arr2)

# #Creating bytes of given size
# bytestr = bytes(4)
# print(bytestr)

# str1 = bytes("Ranjan", "utf-8")
# memoryviewstr = memoryview(str1)
# print(list(memoryviewstr[0:]))

# str2 = bytes("Ranjan", "utf-8")
# see = memoryview(str2)
# print(list(see[0:]))

# num1 = -24.8
# num2 = float(num1)
# num3 = complex(num2)
# num4 = int(num2)
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# multiline_string_is_denoted_by = """
# 1) Ranjan
# 2) kumar 
# 3) singh """
# print(multiline_string_is_denoted_by)

# pie = "ApplePie"
# print(pie[:5])      #Slicing from Start
# print(pie[5:])      #Slicing till End
# print(pie[2:6])     #Slicing in between
# print(pie[-8:])     #Slicing using negative index

# alphabets = "ABCDE"
# for i in alphabets:
#     print(i)

# str1 = " ABcdE FghIJ "
# print(str1.upper())
# print(str1.lower())

# str2 = "Silver Spoon"
# print(str2.replace("Sp", "M")) #the replace() method replaces a string with another string.

# str2 = "Silver Spoon"
# print(str2.split(" "))      #Splits the string at the whitespace " ".

# str2 = "hello WorlD"
# capStr2 = str2.capitalize()
# print(capStr2)

# name = "Ranjan kumar singh"
# print(name.center(60,"-"))
# print(name.count("a"))
# print(name.endswith("kumar"))

# name = "Guzman"
# age = 18
# statement = "My name is {} and my age is {}."
# print(statement.format(name, age)) 

import turtle as tur 
import colorsys as cs
tur.setup(800,800)
tur.speed(5)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done()

# import math as m

# str1 = "Hello \b world !!! "
# print(str1)
