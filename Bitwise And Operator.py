"Q.3Write a program for Bitwise operators"

a=int(input("Enter a First number: "))#---->Take first Input from User
b=int(input("Enter a Second number: "))#----->Take second Input from User

#Bitwise AND Operator
c=a&b
print("The And Operator is: ",c)#---->Print the output of Bitwise AND Operator 

#Bitwise OR Operator
d=a|b
print("The OR Operator is: ",d)#---->Print the output of Bitwise OR Operator

#Bitwise X-OR Operator
e=a^b
print("The X-OR Operator is: ",e)#---->Print the output of Bitwise X-OR Operator

#Bitwise NOT Operator
~a
print("The Not Operator is: ",a)#---->Print the output of Bitwise NOT Operator

#Bitwise Left Shift Operator
a<<1
b<<1
print("a << 1 =", a << 1)#---->Print the output of a and b Bitwise Left Shift Operator
print("b << 1 =", b << 1)

#Bitwise Right Shift Operator
a>>1
b>>1
print("a << 1 =", a >> 1)#---->Print the output of a and b Bitwise Right Shift Operator
print("b << 1 =", b >> 1)

"""<-------------------------------Output----------------------------->
Enter a First number: 67
Enter a Second number: 78
The And Operator is:  66
The OR Operator is:  79
The X-OR Operator is:  13
The Not Operator is:  67
a << 1 = 134
b << 1 = 156
a << 1 = 33
b << 1 = 39"""









