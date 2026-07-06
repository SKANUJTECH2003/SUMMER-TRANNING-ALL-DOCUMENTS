import numpy as np

c=np.array([[1,2,3], [4,5,6]])
d=np.array([[2,4,5], [3,4,6]])

print("APPLYING ALL ARITHMATIC OPERATION ON C & D")
print(c+d)      #SUM OF C & D
print(c-d)      #DIFFERENCE OF C & D
print(c*d)      #PRODUCT OF C & D
print(c/d)      #QUOTIENT OF C & D
print(c//d)     #FLOOR DIVISION OF C & D
print(c**2)     #SQUARE OF C
print(np.sqrt(c)) #SQUARE ROOT OF C
print(np.dot(c,np.transpose(d))) #DOT PRODUCT OF C & D

print("use of sum function")
print(np.sum(c, axis=0)) #SUM OF C ALONG COLUMS
print(np.sum(c, axis=1)) #SUM OF C ALONG ROWS
#chauhandivyank818@gmail.com
#WAP to find fibonacci series 
#WAP  to evalute a string whether it is palandrome or not
#wap to calute the gross income of a salary of a family 
#WAP To make a calculation in wich user desides operator or value 

