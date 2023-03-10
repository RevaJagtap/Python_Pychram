"""
#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
c=lambda a:a+15
print(c(10))
d=lambda x,y:x*y
print(d(2,3))
##########################################################
#2.Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
n=int(input('enter your number:'))
p=lambda x,n:x*n
print(p(n,2))
print(p(n,3))
print(p(n,4))
                ORRRRR
a=lambda x:x*float(input('enter a number'))
print(a(10))
##################################################
#3.Write a Python program to sort a list of tuples using Lambda.
l=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# sort on the basis of num
a= lambda x:sorted(x)
print(a(l))
          OR
c=(sorted(l,key=lambda x:x[0]))
print(c)
b=(sorted(l,key=lambda x:x[1]))
print(b)
#######################################################
#4. Write a Python program to sort a list of dictionaries using Lambda.
d=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
a=(sorted(d,key=lambda x:x['color']))
print(a)
################################################################
#5.Write a Python program to filter a list of integers using Lambda.
l=[2,1,3,5,67,78,8,9]
a=(list(filter(lambda x:x%2==0,l)))
print(a)
b=(list(filter(lambda x:x%2!=0,l)))
print(b)
##############################################################
#6.Write a Python program to square and cube every number in a given list of integers using Lambda.
l=[1,2,3,4,5]
print(list(map(lambda x:x**2,l)))
print(list(map(lambda x:x**3,l)))
          ORRR
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)
########################################################
#7.Write a Python program to find if a given string starts with a given character using Lambda.
s=input('enter your str:')
a=(lambda x:True if x.startswith('R') else False)
print(a(s))
print(a('radha'))
print(a('sadiya'))
###########################################################
#8.Write a Python program to extract year, month, date and time using Lambda.
import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
t=lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))
print(now)
###########################################################################
#9.Write a Python program to check whether a given string is number or not using Lambda.
s='Reva9545'
a=(lambda x:True if x.isnumeric() else False)
b=(lambda x:'is num' if x.isnumeric() else 'Not num') #to get num or not num
print(b(s))
print(a(s))
print(a('12345'))
##########################################################
#10. Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
s=int(input('enter your num:'))
a = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
print(a(s))
print(a(5))
print(a(8))
#######################################################################
#11.Write a Python program to find intersection of two given arrays using Lambda.
a=[1,2,3,4,5,12,13,14]
b=[1,2,3,4,12,7,8,9]
p=(filter(lambda x:x in a,b))
print(list(p))
############################################################
#12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
l1=[-1, 2, -3, 5, 7, 8, 9, -10]
res=list(filter(lambda x:x>0,l1))
res1=list(filter(lambda x:x<0,l1))
result=((sorted(res))+(sorted(res1)))
print(result)
##########################################################
#13.Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
l=[1,2,3,4,5,6,7,8,9,10]
even_count=len(list(filter(lambda x:(x%2==0),l)))
odd_count=(len(list(filter(lambda x:(x%2!=0),l))))
print('even_count=',even_count)
print('odd_count=',odd_count)
########################################################
#14.Write a Python program to add two given lists using map and lambda.
l=[1,2,3]
l1=[4,5,6]
print(list(map(lambda x,y:x+y,l,l1)))
###################################################################
#15. Write a Python program to find the values of length six in a given list using Lambda.
l=['Reva','Prajwalita','Sadiya','Poojaa','Sharvari']
nm=(list(filter(lambda x:x if len(x)==6 else '' ,l)))
print(nm)
#################################################################
#17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
l=[19,38,57,56,39,52,65,85,28]
a=(list(filter(lambda x:x%13==0 or x%19==0,l)))
print(a)
###################################################################
#18.Write a Python program to find palindromes in a given list of strings using Lambda.
l=['aba','madam','java','python']
a=(list(filter(lambda x:(x=="".join(reversed(x))),l)))
print(a)
#################################################################
#19.Write a Python program to find all anagrams of a string in a given list of strings using lambda.
l=['abcd','acbd','adbc','cabd','cat','act','dog','god']
s='cat'
m=lambda x:(''.join(sorted(x))==''.join(sorted(s)))
print(list(filter(m,l)))
                 ORRRR
from collections import Counter
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts))
print("\nAnagrams of 'abcd' in the above string: ")
print(result)
#################################################################
#20.Write a Python program to find the numbers of a given string and store them in a list, display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.
s='sadiya 5 reva 04 sharvari 22 prajwalita 21 pooja 18'
print("Original string: ",s)
s_num=[i for i in s.split(' ')]
lenght=len(s_num)
numbers=sorted([int(x) for x in s_num if x.isdigit()])
print('Numbers in sorted form:')
print(list(filter(lambda x:x>lenght,numbers)))
#############################################################
#21.Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
num=int(input('enter your num:'))
l=[1,2,3,4,5,6]
print(list(map(lambda x:x*num,l)))
##############################################################
"""

