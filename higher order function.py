"""
# Filter function
l=[10,5,9,45,66,67,89,94,31]
odd=lambda num:num%2==1
print(list(filter(odd,l)))
###################################
#PS: filter/fetch name whose len is >5 charachter
l=['reva','sadiya','sharvari','pooja','prajwalita']
sample=lambda name:len(name)>5
print(list(filter(sample,l)))
################################################
#PS: filter/fetch name whose len is >5 charachter
l=['reva','sadiya','sharvari','pooja','prajwalita']
sample=lambda name:name.endswith('i')
print(list(filter(sample,l)))
   OR
l=['reva','sadiya','sharvari','pooja','prajwalita']
print(list(filter(lambda name:name.endswith('i'),l)))
###########################################################
x=lambda n:n+15
print(x(2))
y=lambda a,b:a*b
print(y(3,5))
####################################
####MAP function########
l=['reva','sadiya','sharvari','pooja','prajwalita']
sample=lambda name:name.upper()
print(list(map(sample,l)))
##############################################
k=[2,4,6,8,10]
sample=lambda n:n+100
print(list(map(sample,k)))
   Or
k=[2,4,6,8,10]
print(list(map(lambda n:n+100,k)))
############################################
#Add two lists using map and lambda
num1 = [1, 2, 3]
num2 = [4, 5, 6]
sample= lambda num1,num2:num1+num2
print(list(map(sample,num1,num2)))
################################################
###sal increment 30%
sal=[100000,200000,300000,400000]
sample=lambda sal:sal+sal*0.3
print(list(map(sample,sal)))
#############################################
#Write a Python program to convert all the characters in uppercase and lowercase and eliminate
#duplicate letters from a given sequence. Use map() function.
k=['reva','sadiya','prajwalita','pooja','sharvari','sagar','reva']
sample=lambda k:k.upper()
print(list(map(sample,k)))
sample=lambda k:k.lower()
print(list(map(sample,k)))
s=set(k)
print(list(s))
##############################################################
#Double all numbers using map and lambda
n=[1,2,3,4,5,6]
sample=lambda n:n+n
print(list(map(sample,n)))
################################################
#Write a Python program to convert a given list of tuples to a list of strings using map function.
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
sample =lambda colors:''.join(colors)
print(list(map(sample,colors)))
###############################################################
####Reduce Function######
k=[10,20,30,40,50,60,70]
from functools import reduce
add=lambda x,y:x+y
print(reduce(add,k))
###################################################
l=['reva','sadiya','prajwalita','sharu','pooja']
from functools import reduce
add=lambda x,y:x+y
print(reduce(add,l))
######################################################
k=[1,2,3,4,5,6,7]
from functools import reduce
sample=lambda num1,num2:num1 if num1>num2 else num2
print(reduce(sample,k))
#########################################################
"""

