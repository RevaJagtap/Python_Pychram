"""
#1.Write a Python function to find the Max of three numbers.
num1=int(input('enter your num1:'))
num2=int(input('enter your num2:'))
num3=int(input('enter your num3:'))
def max_of_three(num1,num2,num3):
    if num1>num2 and num1>num3:
        return(num1)
    elif num2>num3 and num2>num1:
        return(num2)
    else:
        return(num3)
print(max_of_three(num1,num2,num3))
print(max_of_three(5,6,7))
                   ORR
max=(lambda x,y,z:x>y and x>z)
print(max(5,2,3))
#########################################################
#2.Write a Python function to sum all the numbers in a list.
l=[1,2,3,4,5]
from functools import reduce
add=lambda x,y:x+y
print(reduce(add,l))
############################################################
#3.Write a Python function to multiply all the numbers in a list.
l=[1,2,3,4,5]
from functools import reduce
multiply=lambda x,y:x*y
print(reduce(multiply,l))
#############################################################
#4.Write a Python program to reverse a string.
s='revajagtap'
def sample(s):
    print(s[::-1])
sample(s)
              ORRRR
#4.Write a Python program to reverse a string.
s='revajagtap'
def sample(s):
    print("".join(reversed(s)))
sample(s)
##########################################
#5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
fact(5)
           OOOOORRRRRRRRRRRRRRRR
num=int(input('enter the no.:'))
def fact(num):
    factorial=1
    if num<0:
        print('It is negative no.')
    else:
        while num>0:
            factorial=factorial*num
            num-=1
        print(factorial)
fact(num)
########################################################################
#6. Write a Python function to check whether a number falls in a given range.
def sample(num):
    if num in range(5):
        print('num is within range',num)
    else:
        print('num is not in range',num)
sample(3)
######################################################
#7.Write a Python function that accepts a string and calculate the number of upper case letters and lower case
s=input('enter your string:')
def letter_count(s):
    uc =lc=0
    for i in s:
        if i.isupper():
            uc+=1
        else:
            lc+=1
    print('count of uppercase letters=',uc)
    print('count of lowercase letters=',lc)
letter_count(s)
###########################################################
#8.Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,2,3,3,3,4,4,5,5,6,7,7,7,8]))
############################################################
#9.Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(num):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
    if c == 2:
        print(num, 'is prime no.')
    else:
        print(num, 'is not prime no.')
prime(4)
##########################################################
#10.Write a Python program to print the even numbers from a given list.
lst=[]
def even_num(l):
    for num in l:
        if num%2==0:
            lst.append(num)
    return lst
print(even_num([1,2,3,4,5,6,7,8,9,12,13,14]))
                 OR
l=[1,2,3,4,5,6,7,8,9,12,13,14]
for num in l:
        if num%2==0:
            print('num is even=',num)
######################################################
#11.Write a Python function to check whether a number is perfect or not.
def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
print(perfect_number(4))
################################################

################################################################
#15.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def square():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    print(l)
square()
#################################################################################
#12.Write a Python function that checks whether a passed string is palindrome or not.
s=input('enter your string:')
if s==s[::-1]:
    print('string is palindrome')
else:
    print('string is not palindrome')
                  ORRR
def palindrome(st):
    c=len(st)-1
    rev_s=''
    while c>=0:
        rev_s=rev_s+(st[c])
        c-=1
    if st==rev_s:
        print(st,'is palindrome')
    else:
        print(st,'not palindrome ')
palindrome('nursesrun')
palindrome('sadiya')
palindrome('madam')
                       ORRR
a=(lambda s:'palindrome'if s==s[::-1] else'not palindrome')
print(a('sir'))
#######################################################
#17. Write a Python program to execute a string containing Python code.
s = 'print("hello world")'
def add(a,b):
    print('addition of two no',a+b)
add(10,20)
print(s)
            ORRRRRR
def dis(s,a,b):

    print(s)
    print("addition of two nos",a+b)
dis("sadiya",10,20)
#####################################################
#15 Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
s='green-red-yellow-black-white'
def sample(s):
    print("-".join(sorted(s.split('-'))))
sample(s='green-red-yellow-black-white')
                    ORRRRRRR
a=s.split('-')
print(a)
p=sorted(a)
print(p)
b=" ".join(p)
print("-".join(sorted(s.split('-'))))
########################################################
#19.Write a Python program to detect the number of local variables declared in a function.
def sample():
    a=10
    b=20
    str='reva'
    l=[1,2,3,4]
    print('hello guys')
print(sample.__code__.co_nlocals)
####################################################################
#13.Write a Python function to check whether a string is a pangram or not.
def panagram(str):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in str.lower():
            return ('not panagram')
        else:
            return (' str is panagram')
print(panagram('"The quick brown fox jumps over the lazy dog"'))
#########################################################################
"""
#16.Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
















