"""
#PS-Give the list of 0-10 squared numbers
print([i**2 for i  in  range(11)])
#######################################
#PS-Give the list of upper lower function
k=['riya','siya','priya','shiya','piya']
print([i.lower() for  i  in k])
print([i.upper() for  i  in k])
##########################################
# PS-display all even numbers from 1 to 40
print([i for i in range(1,41) if i%2==0])
##############################################
#Find all of the numbers from 1–1000 that are divisible by 8
print([i for i in range(1,1001) if i%8==0])
#######################################################
#Find all of the numbers from 1–1000 that have a 6 in them
print([i for i in range(1,1001) if '6' in str(i)])
##########################################################
#Count the number of spaces in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
t=[i for i in string if i==' ']
print(len(t))
###################################################
#Remove all of the vowels in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
vowels=['a','e','i','o','u']
t=[i for i in string if i.lower() not in vowels]
result=''.join(t)
print(result)
#########################################################
        OR
string = "Practice Problems to Drill List Comprehension in Your Head."
result=([i for i in string if i not in ['a','e','i','o','u']])
print(result)
print(''.join(result)
#################################################################
#Find all of the words in a string that are less than 5 letters (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
result=([i for i in string.split(' ') if len(i)<5])
print(result)
                       OR
string = "Practice Problems to Drill List Comprehension in Your Head."
m=string.split()
print(m)
p=([i for i in m if len(i)<5])
print(" ".join(p))
################################################################
"""








