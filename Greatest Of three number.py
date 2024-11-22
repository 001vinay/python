"Q.4 Write a program to calculate greatest of three numbers."

a=int(input("Enter first number: "))#---->Taking First Input from user
b=int(input("Enter second number: "))#---->Taking First Input from user
c=int(input("Enter third number: "))#---->Taking First Input from user

if(a>b):#----->use nested-if condition for finding the greater number
   if(a>c):
       g=a
   else:
    g=c

else:
    if(b>c):
        g=b
    else:
     g=c
print("The greater number is: ",g)#----->Print the output of Greater number
    
"""<----------------------------Output--------------------------->
Enter first number: 67
Enter second number: 09
Enter third number: 98
The greater number is:  98"""
