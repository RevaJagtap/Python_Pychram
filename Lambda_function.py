"""
sq=lambda num:num*num
print(sq(21))
#############################################
from math import sqrt
root=lambda num:sqrt(num)
print(root(4))
##############################################
from math import pi
area=lambda r:(pi*r**2)
print(round(area(4),2))###it gives the output upto 2 digit
#############################################################
##Lambda using positional argument
add=lambda x,y:x+y
print(add(5,9))
###########################################################
##Lambda using keyword argument
sub=lambda x,y:x-y
print(sub(x=300,y=350))
##############################################################
##Lambda using default argument
conv=lambda nm='guest':nm.upper()
print(conv())
print(conv('reva'))
##################################################################
"""
