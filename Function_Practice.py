"""
def add():####Function declaration and calling.
    print(20+56)
add()
############################
def add(x,y):
    print(x+y)
x=20
y=60
add(x,y)
add(20,54)
add(20.5,30.5)
##################################
def add(x,y):
    x=10
    y=30,###Local value when they are present then it does not take globsl valur from outside
    print(x+y)
x=20
y=60
add(x,y)
add(20,54),#####Global value it will take when local value not present..
add(20.5,30.5)
#########################################################
a = 20
b = 40
def add():
    print('Inside:',a+b)
add()
print('Outside:',a+b)
###########################################################
a=10
b=20
def add():
    a=5
    b=6
    print(a+b)
print(a+b)
add()
print(a+b)
##################################
k=[10,20,34,48,53]
def sample(k):
    print(min(k))
sample(k)
##################################
k=[10,20,4,48,53]
def sample(k):
    k.sort()
    print(k)
    print(k[0])
sample(k)
###################################
x = 100
def sample():
    x=45
    x = x + 100
    print(x)
sample()
############################################
x = 40
def sample():
    global x
    x = x + 40
    print(x)
sample()
print(x)
To change global value x then use (global x) word
###############################################
def sample():
    pass
print(sample())
#################################################
def sample():
    return'Reva'
print(sample())
################################################
def substraction():
    return 10-50
print(substraction())
result=substraction()
print(result)
result1=substraction()
print(result1)
#########################################
def sample():
    e=100
    b=200
    c=300
    return (b*c-e)
print(sample())
##########################################
st='Reva JaGtaP'
def ltr_count(st):
    uc=0
    lc=0
    for i in st:
        if i.isupper():
            uc += 1
        else:
            lc += 1
    print('number of upper case ltrs =',uc)
    print('number of lower case ltrs =',lc)
ltr_count(st)
####################################################
def info(student,college,branch):
    print('student:',student)
    print('college:',college)
    print('branch:',branch)
info('reva','DYP','Mech')
#################################
s='reva9545'
def sample(s):
        return s[::-1]
print(sample(s))
####################################
st = input('enter string = ')
def rev(st):
    print(st[::-1])
rev(st)
########################################
def sample(a,b,c):
    print(a[::-1])
    print(b[::-1])
    print(c[::-1])
sample('reva','pooja','sadiya')
######################################
def sample(a,b,c):
    print(''.join(list(reversed(a))))
    print(''.join(list(reversed(b))))
    print(''.join(list(reversed(c))))
sample('reva','pooja','sadiya')
#############################################
##########################
l=[1,2,3,4,5]
def sample(l):
    s=1
    for i in l:
        s=i*s
    print(s)
sample(l)
#################################################
l=[1,2,3,4,5]
def sample(l):
    s=0
    for i in l:def fact(nm):
    factorial=1
    for i in range (1,nm+1):
        factorial=factorial*i
    print(factorial)
fact(5)

        s=i+s
    print(s)
sample(l)
###################################################
def sample(num):
        if num in range(20):
            print('num within range',num)
        else:
            print('num outof range',num)
sample(num=34)
sample(num=2)
sample(num=41)
#########################################################
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))
###################################################
def sample(l):
    print(list(set(l)))
sample(l=[1,2,3,4,4,3,7,8,9,9,8,7,])
#####################################################
#Default Argument:
def info(menu,hotel='punkaj'):
    print(menu,hotel)
info('pulav')
info('rice','taj')
info('roti','alankar')
###############################
#Keyword argument:
def info(village,distric,state):
    print('village:',village)
    print('district:',distric)
    print('state:',state)
info(village='kodoli',distric='satara',state='Maharastra')
#############################################
#When non-default argument follows default argument its not allowed as per syntax.
def info(place='Maharashtra',name):#name is positional/non default argument,place=m is default argu.
    print(name,place)
info('Ankush')
info('Ganesh','Kolhapur')
##########################################
def show(p,q,r=400):
    print(p,q,r)
# in above case p,q are positional args
# r is default arg.
# so r should always follow p,q
show(34,60)
#############################################
#variable length argument:
def sample(*IT_course):
    print('IT_course',IT_course)
sample('data_science')
sample('machine_learning')
sample('python')
###########################################
###variable length keyword:
def info(**family):
    print('group of family',family)
info(shiv='1',yug='2',reva='28')
info(s='23',v='34',p='38',r='28')
################################################
"""
