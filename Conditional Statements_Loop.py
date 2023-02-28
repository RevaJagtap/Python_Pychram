"""
#Take values of length and breadth of a rectangle from user and check if it is square or not.
l=20
w=20
sqr=l*w
if l==w:
    print('square')
else:
    print('not square')
################################
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print percentage of class attended
Is student is allowed to sit in exam or not.
a=classes_held=int(input('no.of classes held:'))
b=classes_attended=int(input('no.of classes attended:'))
attendance=b/a
per=(b/a)*100
print(attendance*100)
if per>75:
    print('eligible for exam')
else:
    print('not eligible')
########################################################
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
marks=float(input('enter your marks:'))
if marks>80:
    print('grade A')
elif marks in range(60,80):
    print('grade B')
elif marks in range(50,60):
    print('grade C')
elif marks in range(45,50):
    print('grade D')
elif marks in range(25,45):
    print('grade E')
else:
    print('fail')
#############################################################
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
l=[]
for i in range(1500,2701):
    if (i%7==0) and (i%5==0):
      l.append(i)
print(l)
######################################################################
#Write a Python program to guess a number between 1 to 9.
num=int(input('enter your num:'))
if num<10:
    print('well guessed')
else:
        print('wrong guessing')
################################################################
#Write a Python program to count the number of even and odd numbers from a series of numbers.
num=[1,2,3,4,5,6,7,8,9,10,11]
count_odd=0
count_even=0
for num in range(1,12):
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
print('count of even num',count_even)
print('count of odd num',count_odd)
#######################################################
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
l=[]
for i in range(0,7):
    if i%3!=0:
        l.append(i)
print(l)
                 OR Best solution
for i in range(7):
    if (i==3 or i==6):
        continue
    else:
        print(i)
print('output ok')
####################################################################
#Write a Python program that accepts a string and calculate the number of digits and letters.
s=input('enter your string:')
letter=0
digit=0
for i in s:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        'blank'
print('number of digit',digit)
print('number of letter',letter)
############################################
#Write a Python program to find numbers between 100 and 400(both included) where each digit of a number is an even number.The numbers obtained should be printed in a comma - separated sequence.
l=[]
count_even=0
for i in range(100,401):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        l.append(s)
print(",".join(l))
#######################################################################
#Write a Python program to check whether an alphabet is a vowel or consonant.
letter=input('enter your letter:')
if letter in ('a','e','i','o','u'):
    print('its vowel',letter)
else:
    print('it is consonant')
           ####ORRRR####
letter=input('enter your letter:')
if letter in 'aeiou':
    print('its vowel',letter)
else:
    print('it is consonant',letter)
################################################
#Write a Python program to convert month name to a number of days
month_list=('jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec')
month=input('enter your month:')
if month=='feb':
    print('28/29 days of month')
elif month in ('apr','jun','sept','nov'):
    print('30 day of months')
elif month in ('jan','mar','may','jul','aug','oct','dec'):
    print('31 days of months')
else:
    print('no matching month')
#########################################
#Write a Python program to get the Fibonacci series between 0 to 50.
num1=0
num2=1
num3=0
while num3<50:
    num3=num1+num2
    num1=num2
    num2=num3
    if num3<50:
        print(num3,end=",")
###########################################
Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
temp=int(input('enter your temp :'))
unit=input('enter your unit:')
if unit=='f':
    fahr = (temp * 9 / 5) + 32
    print(fahr)
else:
    cels = (temp - 32) * 5 / 9
    print(cels)
################################################
#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,51):
    if i%3==0 and i%5==0:
        print('fizzBuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
############################################################
#Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
row=int(input('enter your row_num:'))
col=int(input('enter your col_num '))
l=[]
for i in range(0,row):
    l.append([])
    for j in range(0, col):
       l [i].append(i*j)
print(l)
#######################################################
#Write a Python program that accepts a word from the user and reverse it.
s='reva'
l=[]
a="".join(list(reversed(s)))
l.append(a)
print(l)
        OR
print("".join(list(reversed(s))))
#########################################
#Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print(type(i),i)
###########################################
#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
s=input('enter your sequence:')
for i in s.lower():
    print(i,end="")
      OR
s=input('enter your sequence:')
for i in s:
    print(i.lower(),end="")
##########################################################
#Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
a= '0100,0011,1010,1001,1100,1001'
items = []
for p in a.split(','):
    x = int(p,2)
    if x%5==0:
        items.append(p)
print(','.join(items))
###########################################################
#Write a Python program to check the validity of password input by users.
   # Validation :At least 1 letter between [a-z] and 1 letter between [A-Z].
                # At least 1 number between [0-9].
                # At least 1 character from [$#@].
                # Minimum length 6 characters.
                # Maximum length 16 characters.
pwd = input("enter your password")
sp_char = ['!','@','.']
count_low = count_upp = count_sp = count_dig = 0
if len(pwd) in range(6,16):
    for i in pwd:
        if i.islower():
            count_low += 1
        elif i.isupper():
            count_upp += 1
        elif i.isdigit():
            count_dig += 1
        elif i in (sp_char):
            count_sp  +=1
if count_low >= 1 and count_upp >=1 and count_dig >= 1 and count_sp>=1:
    print("valid password")
else:
    print('wrong password')
#################################################################
#Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
        # Note :# An equilateral triangle is a triangle in which all three sides are equal.
        # A scalene triangle is a triangle that has three unequal sides.
        # An isosceles triangle is a triangle with (at least) two equal sides.
a=float(input('enter your first side:'))
b=float(input('enter your second side:'))
c=float(input('enter your third side:'))
for i in (a,b,c):
    if a==b==c:
        print('its equilateral triangle')
    elif a!=b!=c:
        print('its scalene triangle')
    else:
        print('its isosceles triangle')
###################################################################
#Write a Python program to find the median of three values
a=int(input('enter your 1st value:'))
b=int(input('enter your 2nd value:'))
c=int(input('enter your 3rd value:'))
print('median of above three numbers')
if a<b and b<c:
    print(b)
elif c<a and a<b:
    print(a)
elif a<c and c<b:
    print(c)
      OR
l=[1,2,3,4,5,7,6,8,9,10]
a=(sorted(l))
print(a)
m=(len(l)+1//2)
print(m)
#######################################################
Challenge 1: Write a function which:
# - Takes a string as an argument
# - returns the string in all upper case if its' length is even, and all lower case if its' length is odd. Any non-alphabetic characters should not be changed
# - stretch goal: try to implement this both with and without the .upper()/.lower()
methods

def func_1_methods(string):
    pass

def func_1_no_methods(string):
    pass
******************************
Str1=input("Enter the string to be converted uppercase: ")
def upper
Str1=input("Enter the string to be converted uppercase: ")
def upper(Str1):
    y = ''
    for i in range (0,len(Str1)):
       x=ord(Str1[i])
       if x>=97 and x<=122:
           x=x-32
       y+=chr(x)
    print(y,end="")
def lower(Str1):
    y=''
    for i in range(0, len(Str1)):
        x = ord(Str1[i])
        if x >=65  and x <= 91:
            x = x +32
        y += chr(x)

    print( y, end="")
if len(Str1)%2==0:
    upper(Str1)
else:
    lower(Str1)
#########################################################################
Write a Python program to calculate a dog's age in dog's years. Go to the editor
   # Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
h_age = int(input())
def human_years(h_age):
    if h_age < 0:
        print('enter postive number')
    elif h_age <= 2:
        d_age = 10.5 * h_age
    else:
        d_age = 21 + (h_age - 2) * 4
    return ('dog age is', d_age)


#human_years(h_age)
#############################################################
#Write a Python program to find the median of three values.
t = [10,9,8,5,4,3,2,9,8,9]
def median(t):
    t.sort()
    l = len(t)
    if l%2 == 0:       # even
        y1 = int((l/2)+0.5)
        y2 = int((l/2)-0.5)
        y = (t[y1]+t[y2])/2
        print(y)
    else:                  #odd
        i = int(l/2+0.5)-1   #to find middle index
        z = t[i]
        return z

median(t)
##############################################################
#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sum_integer(num1,num2):
    if (num1+num2)in range(15,21):
        return(20)
    else:
        return('None')
print(sum_integer(12,7))
##########################################################
#Write a Python program to check a string represent an integer or not.
s=input('enter your string:')
if s.isnumeric():
    print('string is an integer')
else:
    print('string is not integer')
########################################################
#Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March') and (day in range(1,31)):
	print('season=winter')
elif month in ('April', 'May', 'June') and (day in range(1,31)):
	print('season=spring')
elif month in ('July', 'August', 'September') and (day in range(1,31)):
	print('season=summer')
else:
	print('season=autumn')
###################################################################
#Write a Python program to create the multiplication table (from 1 to 10) of a number.
n=int(input('enter your number:'))
for i in range(1,11):
    print (n,'x',i,'=',n*i)
##########################################################################
