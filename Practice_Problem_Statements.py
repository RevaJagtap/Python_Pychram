"""
#Write a program to print every character of a string entered by the user in a new line using a loop.
s=(input('enter your string:'))
for i in s:
    print(i)
            ORRR
s=input("enter the string")
for i in range(len(s)):
    print(s[i],i)
###############################################################################
#Write a program to find the length of the string "machine learning" with and without using len function.
s='machine learning'
print(len(s))   ###with len function
c=0   ### without len
for i in s:
    c+=1
print(c)
c=0   ### without len
while s[c:]:
    c+=1
print(c)
################################################################
#Write a program to check if the word 'orange' is present in the "This is orange juice".
s='This is orange juice'
for i in s.split():
    if i=='orange':
        print('present in given str')
          ORRRRRR
s='This is orange juice'
i='orange'
if i in s:
    print('present in given str')
else:
    print('not present')
                    ORRRR
print(['present'for i in s.split() if i=='orange'] )
#################################################################
#Write a program to find the number of vowels, consonants, digits, and white space characters in a string.
s='hello Reva 9545'
v=0
c=0
d=0
w=0

vowel="aeiou"
for i in  s:
    if i.isdigit()==True:
        d=d+1
    elif i.isspace()==True :
        w=w+1
    elif i in vowel:
        v=v+1
    elif i not in vowel:
        c=c+1

print("digits",d)
print("vowels",v)
print("consonant",d)
print("white space",w)
################################################################
#Write a Python program to count Uppercase, Lowercase, special character,and numeric values in a given string.
#s='Reva@Jagtap9545'
#######################################################################
#Write a Python program to remove the nth index character from a non-empty string.
s=input('enter your string:')
index=int(input('enter your index:'))
for i in range(len(s)):
    if i==2:
        continue
    print(i,s[i])
##################################################################
#Write a Python program to change a given string to a new string where the first and last characters have been exchanged.
str='RevaJagtap'
print(str[-1] + str[1:-1] + str[0])
#########################################################################
#Write a Python program to count the occurrences of each word in a given sentence.
from collections import Counter
s='Revajagtap'
a=Counter(s)
print(a)
                  ORRRRR
s='RevaJagtap'
n=""
c=1
for i in s:
    if i in n:
        c+=1
        print(i,c)
    else:
        n+=i
        print(i,1)
#######################################################
#Write a program to find last 10 characters of a string?
s='India is my country.India is the best'
s1='My name is reva vikram jagtap'
print(s[-10:])
print(s1[-10:])
###########################################################
#WAP to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
s="ManGo is sweet"
c=0
for i in s[:5]:
    if i.isupper():
        c=c+1
if c>=2:
    print(s.upper())
else:
    print(s)
##############################################################
#Write a Python program to remove a newline in Python.
s='Python is very intresting language'
for i in s:
    print(i,end='')
##############################################################
#Write a Python program to swap commas and dots in a string
s= "32.054,23"
a=(s[0:2]+s[-3]+s[3:6]+s[2]+s[7:])
print((a))
                      OR
s= "32.054,23"
s=s.replace(".","@")
print(s)
s=s.replace(",",".")
print(s)
s=s.replace("@",",")
print(s)
########################################################
#Write a Python program to find the first repeated character in a given string.
s='hello good mornig'
def repeated_char(s):
    s1=''
    counter=0
    for i in s:
        if i in s1:
            print('first repeated char is',i )
            break
        else: s1=s1+i
repeated_char(s)
#######################################################
#Write a Python program to find the second most repeated word in a given string.
s='hi hello how are you who are you'
e =''
res=[]
for i in s.split():
    #print(i)
    if i in e:
        res.append(i)
    else:
        e=e+i
print(''.join(res[1]))
#########################################################
#Python program to Count Even and Odd numbers in a string.
s='123456789'
even=0
odd=0
a=s.split()
for i in "".join(a):
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
print("odd count",odd)
print("even no",even )
###########################################################
#How do you check if a string contains only digits?
s=input('enter your string:')
if s.isdigit():
    print("s contains all numbers")
else:
    print("s doesn't contains all numbers")
#########################################################
#How do you remove a given character/word from String?
s='Revajagtap'
for i in s:
    if i.replace('a',''):
        print(i,end='')
          solution for word
s='reva jagtap kodoli'
a=s.split()
for i in a:
    if i.replace('reva',''):
        print(i,end='')
########################################################
#How do you remove a given character/word from String?
s="Reva"
char=input("enter char to be removed:")
for i in s:
    #print(i)
    if i==char:
        continue
    else:
        print(i,end="")
          #####Solution for word remove######
str = " hi Reva how are you"
sub = input('enter the string')
for i in str.split():
    if i == sub:
        continue
    else:

        print(i, end=" ")
###########################################################
# Write a Python program to remove the characters which have odd index values of a given string.
s='python is case sensitive language'
s1=""
for i in range(len(s)):
    if i%2==0:
        s1=s1+s[i]
print(s1)
           Or
print(s[::2])
################################################################################
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(6):
    if (i==3 or i==6):
        continue
    else:
        print(i)
print('output ok')
##################################
Write a Python program that accepts a word from the user and reverse it.
s='reva'
def sample(s):
    return s[::-1]
print(sample(s))
222222
s='yugandhar'
def rev():
    print(''.join(reversed(list(s))))
rev()
#######################################################
Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for x in range(1500,2701):
    if x%7==0 and x%5==0:
        print(x)
print()
#####If i want op in the form of list then
l=[]
for x in range(1500,2701):
    if (x%7==0 )and (x%5==0):
        l.append(x)
print(l)
########################################
Write a Python program to convert temperatures to and from celsius, fahrenheit.
tmp = float(input('enter temp = '))
unit = input('enter unit to convert = ').lower()
def conv(tmp):
    if unit == 'f':
        T = ((tmp/5)*9) + 32
        return T
    elif unit == 'c':
        T = ((tmp-32) * 5) / 9
        return T
    else:
        print('enter proper choice')
print(conv(tmp))
########################################
Write a Python program that accepts a string and calculate the number of digits and letters.
s='Raya2020'
l=d=0
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        print('anything')
print('digit',d)
print('letter',l)
################################################
str='pooja tibile 180892'
lst1=[]
lst2=[]
for i in str:
    if i.isalpha():
        lst1.append(i)
    elif i.isdigit():
        lst2.append(i)
print(''.join(lst1),len(lst1))
print(''.join(lst2),len(lst2))
####################################
s='Raya2020'
for i in s:
    if i.isdigit()==True:
        print('value is digit',i)
    elif i.isalpha()==True:
        print('value is letter',i)
    else:
        print('anything')
print('raya2020')
#############################################
Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
###########################################
starts_with = lambda strr : True if strr.startswith('j') else False
print(starts_with('jay'))
#########################################
s='reva jagtap pin: 9545'
for i in s:
 if i.isdigit()== True:
     print(i,end='')
##############################################
#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array1234(nums):
    for i in range(len(nums)-3):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3 and nums[i+3]==4 :
            return True
    return False
print(array1234([1,2,3,4,5]))
########################################################
tmp = float(input('enter temp = '))
unit = input('enter unit to convert = ').lower()
def conv(tmp):
    if unit == 'f':
        T = ((tmp/5)*9) + 32
        return T
    elif unit == 'c':
        T = ((tmp-32) * 5) / 9
        return T
    else:
        print('enter proper choice')
print(conv(tmp))
####################################################
# Python program to sort Python Dictionaries by Keys
dict={'Reva':'Mech','Pooja':'ENTC','Sadiya':'IT'}
for key in sorted (dict):
    print(key,end=" ")
####################################################
#Python program to sort Python Dictionaries by Values
dict={'Reva':'Mech','Pooja':'ENTC','Sadiya':'IT'}
print(sorted (dict.values()))
          ORRRRRR
for values in sorted (dict.values()):
    print(values,end=" ")
##############################################
#3.Python program to find the sum of all items in a dictionary
d={'sample1':200,'sample2':130,'sample3':250,'sample4':450}
print(sum(d.values()))
#################################################
#4. Python program to remove a key from a dictionary
dict={'Reva':'Mech','Pooja':'ENTC','Sadiya':'IT'}
m=dict.pop('Reva')
print(dict)
###############################################
#Python program to merge two Dictionaries
d1={1:200,2:300,3:400,4:500}
d2={'a':10,'b':20,'c':30,'d':40,'e':50}
d=d1.copy()
d.update(d2)
print(d)
################################################
# Python program to convert a list of Tuples into Dictionary
s=[('a',12),('b',23),('c',45),('d',65)]
print(dict(s))
                     ORR
print({ i[0]:i[1] for i in lst })
########################################################
# Program to create grade calculator in Python
percentage=float(input('enter your marks:'))
if percentage>=80:
    print('First class with distinction')
elif percentage in range(60,80):
    print('First class')
elif percentage in range(50,60):
    print('Second class')
elif percentage in range(40,50):
    print('Third class')
else:
    print('fail')
                ORRRR
marks=[]
for i in range(5):
    marks.append(int(input("enter marks one by one:")))
print(marks)
total=sum(marks)
print(total)
avg=total/len(marks)
print(avg)
result=input(("enter your avg"))
if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
              ORRRRR
roll_no=int(input('enter your roll no:'))
student_name=input('enter student name:')
marks=eval(input('enter your marks:'))
total_marks=sum(marks)
percentage=(total_marks/500)*100
if percentage>=90:
    print(percentage)
    print('grade A')
elif percentage>=80:
    print(percentage)
    print('grade B')
elif percentage>=70:
    print(percentage)
    print('grade C')
elif percentage>=60:
    print(percentage)
    print('grade D')
elif percentage>=50:
    print(percentage)
    print('grade E')
elif percentage>=40:
    print(percentage)
    print('pass')
else:
    print('fail')
######################################################
#Print anagrams together in Python using List and Dictionary.
l=['bag','tab','bat','gab']
d={}
for i in l:
    a="".join(sorted(i))
    if a in d:
        d[a].append(i)
    else:
        d[a]=[i]
print(d)
print(list(d.values()))
############################################################
#Python Counter to find the size of the largest subset of anagram words.
l=['bag','tab','bat','gab','abg']
d={}
for i in l:
    a="".join(sorted(i))
    if a in d:
        d[a].append(i)
    else:
        d[a]=[i]
print(d)
print(list(d.values()))
var=d.values()
m=sorted(var,key=len)
print(len(m[-1]))
                   ORRRR
from collections import Counter
inp = 'ant magneta magneta tan magneta ganmeta'
def anagram_words(inp):
    s=inp.split(" ")
    for i in range(0,len(s)):
        s[i]="".join(sorted(s[i]))
    m=Counter(s)
    print(m)
    print(max(m.values()))
anagram_words(inp='ant magneta magneta tan magneta')
###############################################################
#Counting the frequencies in a list using a dictionary in Python
s=['praju','pooja','praju','praju','pooja','reva']
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
####################################################
#Create a list of tuples from the given list having a number and its cube in each tuple.
l=[1,2,3,4,5,6]
lst=[]
def list_tuple_cube(l):
    for i in l:
        lst.append((i,i**3))
    print(lst)
list_tuple_cube(l)
             ORR
lst=[1,2,3,4]
print(list(map(lambda x:(x,x*x*x),lst)))
            ORRR
result = [(i, i**3) for i in lst]
print(result)
########################################################
#Sort a list of tuples by the second Item
l=[(1,20),(3,10),(2,45),(5,78)]
def sort_tup_second_item(l):
    return(sorted(l,key=lambda x:x[1]))
print('sorted list',sort_tup_second_item(l))
                 #ORRRR
print(sorted(l,key=lambda x:x[1]))
#########################################
#Python Program for Find largest prime factor of a number.
n=int(input('enter the no.:'))
lst=[]
for i in range(1,n+1):
    if n%i==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        if count==2:
            lst.append(i)
print(lst)
print('largest prime factor of',n,'is',max(lst))
#####################################################
#Python Program for Product of unique prime factors of a number
n=int(input('enter the no.:'))
product=1
for i in range(2,n+1):
    if (n % i == 0):
        isPrime = 1
        for j in range(2, int(i / 2 + 1)):
            if (i % j == 0):
                isPrime = 0
                break
    if (isPrime):
        product = product * i
print(product)
########################################################
#Python Program for Largest and Smallest K digit number divisible by X
num=95
k=7
n=1
while n>0:
    a=num*n
    if len(str(a))==7:
        break
    else:
        n+=1
print(a)
########################################################
"""


