"""
#Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 4, 3: 8, 4: 5, 2: 6, 0: 7}
print(sorted(d.items(), key = lambda x: x[1], reverse = True))
print(dict((sorted(d.items(), key = lambda x: x[1], reverse = True))))
print(sorted(d.items(), key = lambda x: x[1]))
print(dict((sorted(d.items(), key = lambda x: x[1]))))
##########################################################
d = {1: 4, 3: 8, 4: 5, 2: 6, 0: 7}
value_asce=sorted(d.items(),key= lambda x:x[1])
value_disc=sorted(d.items(),key= lambda x:x[1],reverse=True)
print ('ascending by value',dict(value_asce))
print ('descending by value',dict(value_disc))

key= sorted(d.items())
print ('ascending by key',dict(key))
disc=sorted(d.items(),reverse=True)
print('descending by key',dict(disc)
##############################################
#Write a Python script to add a key to a dictionary
d= {0: 10, 1: 20}
(d.update({2:30}))
print(d)
##############################################
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
num=int(input('enter your num:'))
dict=dict()
for i in range(1,num+1):
  dict[i]=(i*i)
print(dict)
############################################
             OR
d2 = { i :(i*i) for i in range(1,21) }
print(d2)
#######################################
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic={}
for d in(dic1,dic2,dic3):dic.update(d)
print(dic)
###########################################
                OR
d1.update(d2)
print(d1)
d1.update(d3)
print(d1)
########################################
#Write a Python script to check whether a given key already exists in a dictionary.
d={1:10,2:20,3:30,4:40,5:50}
key=int(input('enter key:'))
if key in d:
    print('key is present')
else:
    print('key not present')
#################################################
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d=dict()
for i in range(1,16):
  d[i]=i**2
print(d)
#############################################################
sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)
########################################################
"""





