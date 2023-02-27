"""
name='tiger'
animal = input('enter the animal:')
if animal == 'tiger':
    print('wild animal')
elif animal == 'cat':
    print('pet animal')
elif animal == 'dog':
    print('cute one')
else:
    print('king of animals')
############################################
saree=input('enter your choice:')
if saree =='silk saree':
    print('heavy')
elif saree == 'cotton':
    print('medium')
elif saree =='brasso':
    print('affordable')
else:
    print('other choice')
################################################
print('enter your marks:\n1.90,\n2.85,\n3.78,\n4.65')
marks=input('marks:')
if marks=='90':
    print('topper')
elif marks=='85':
    print('second')
elif marks=='78':
    print('third')
elif marks=='65':
    print('avrage')
else:
    print ('fail')
################################################
print('enter your wt:\n1.23,\n2.45,\n3.67:')
wt=input('wt')
if wt =='1':
   print('too low')
elif wt =='2':
   print('meduim')
elif wt == '3':
   print( 'fatty')
else:
   print('corrct weight')
###############################################
num=int(input('enter your num:'))
if num<=0:
    print('num is negative')
elif num>=0:
    print('num is positive')
else:
    print('check other condition')
##################################################
num=int(input('enter ur num:'))
if num<=9:
    print('this is 1 digit num')
elif num<=99:
    print('this is 2 digit num')
elif num<=999:
    print('this is 3 digit num:')
else:
    print('invalid num')
##########################################################
s='I love my India'
if 'india' in s:
    print('s')
else:
    print('not present')
#######################################################
s= 'ABC PQR' # 'ABC PQR' S[::-1]= 'RQP CBA' s.split()
j = s.split()
n= ((' '.join(j[::-1])))
print(n)
print(n[::-1])
################################################
s= 'ABC PQR'
m=s.split()
print(m)
for i in m:
    print(i[::-1],end=" ")
############################################
for i in range(1,101,2):
    print(i,end=',')
print(list(range(1,101,2)))
#############################################
for num in range(1,101):
    print(num,end=',')
####################################################
s='Python is very simple'
for i in s:
    print(i,end=',')
###################################
s='Python is very simple'
for i in s:
    print(i)
#########################################
s='reva jagtap pin: 9545'
pin= s.split(':')
print(pin[-1])
##############################################
s='reva jagtap pin: 9545'
for i in s:
 if i.isdigit()== True:
     print(i,end=''
#################################################
num=int(input("enter the no:"))
if num>1:
    for i in range(2,num):
        if num%i==0  :
            print("no is not prime no:",num)
            break
        else:
            print("no is prime no:",num)
##################################################
nm=int(input('enter no.:'))
if nm==2 or nm==3:
    print(nm,'is prime no.')
elif nm%2 == 0 or nm%3 ==0:
    print(nm,'is not prime no.')
else:
    print(nm,'is prime no.')
##############################################################
r=[10,27,35,48,45,42,56,50]
s=[]
for num in r:
    if (num % 5==0) or (num % 7== 0):
        print(num)
        s.append(num)
print('final list is:',s)
###############################################





for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=' ')
    print()
##################################################
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=' ')
        print()
###################################################
k=1
for i in range(1,11):
    for j in range (1,11):
        print(j*k,end=' ')
    print()
    k=k+1
####################################################
for i in range(1,11):
    for j in range(1,4):
        print((j*10)+i,end=' ')
    print()
############################################
for i in range(1,11):
    for j in range(11,21):
        print(i*j,end=' ')
    print()
##############################################
num=1
while num<10:
    print(num)
    num=num+1
###############################################
num=11
while num>0:
    print(num)
    num=num-1
###############################################
num=1
while num==1:
    print('python')
    num=2
################################################
r='reva'
while 'v' in r:
    print('its present')
    r= 'gata'
######################################################
num=int(input('enter the num:'))

while num>0:
    if num%2 == 0:
        print('even')
    else:
        print('odd')
    num=num-1
############################################
num=20
while num==20:
    if num%2 == 0:
        print('even')
    else:
        print('odd')
    num=21
##################################################
num = 20
while num > 0:
    if num %2 == 0:
        print('Even:',num)
    else:
        print('Odd:',num)
    num-=1
###################################################
even=[]
odd=[]
num = 1
while num <10:
    if num %2 == 0:
        #print('even',num)
        even.append(num)
    else:
        #print('odd',num)
        odd.append(num)
    num=num+1
print('even list',even)
print('odd list',odd)
################################################
even=[]
odd=[]
num = 1
while num <10:
    if num %2 == 0:
        print('even',num)
        even.append(num)
    else:
        print('odd',num)
        odd.append(num)
    num=num+1
print('addition of even list',sum (even))
print('addition of odd list',sum (odd))
###########################################
s="Reva1234"
c=0
le=len(s)
while c<len(s):
    if s[c].isalpha():
        print(s[c],'is char')
    elif s[c].isdigit():
        print(s[c], 'is a number')
    else:
        print(s[c], 'is special character')
    c += 1
##############################################
k=['rs','fgre345','@$']
c=0
while c< len(k):
    #print(C)
    #print(k[c])
    for i in k[c]:
        if i.isalpha():
            print(i, 'is char')
        elif i.isdigit():
            print(i, 'is a number')
        else:
            print(i, 'is special symbol')
    c += 1
#############################################
k=['fdgre','bank1234','#$%@6fhyrt','168493']
c=0
while c<len(k):
    for i in k[c]:
        if i.isalpha():
            print(i,'is char')
        elif i.isnumeric():
            print(i,'is number')
        else:
            print(i,'is special char')
    c+=1
##################################################
fruits = ['mango','orange','Banana','Apple','orange']
for i in fruits:
    if i == 'Banana':
        break
    else:
        print(i)
####################################
fruits = ['mango','Orange','Banana','Apple','Orange']
Orange_c=fruits.count('Orange')
c=0
for i in fruits:
    if i == 'Orange':
        c+=1
        if i=='Orange' and c== Orange_c:
           break
        else:
           print(i)
    else:
        print(i)
##########################################
s='Reva'
for i in s:
    if i== 'v':
        break
    else:
        print(i)
##############################################
for i in range(69):
    if i == 57:
        exit()
    else:
        print(i)
#####################################################
for i in range(69):
    if i == 57:
        continue
    else:
        print(i)
print('op')
#######################################################
for i in range(69):
    if i == 57:
        break
    else:
        print(i)
print('op')
#####################################################
#1-10
num=1
while num<11:
    print('number is:',num)
    num+=1
########################################
#10-1
num=10
while num>0:
    print('number is:',num)
    num-=1
#######################################
#10-1 addition
num=1
s=0
while num<11:
    #print(num)
    s=s+num
    num=num+1
print(s)
#######################################
#10-1
num=10
while num>0:
    print('number is:',num)
    num-=2
##############################################
#Even Odd
num=int(input('enter your num:'))
while num<11:
    if num%2==0:
        print('num is even',num)
    else:
        print('num is odd',num)
    num+=1
################################################

"""
odd=[]
even=[]
num=10
while num>0:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
    num-=1
print('odd list:',odd[::-1])
print('even list:',even[::-1])




