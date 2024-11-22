a=20  #------->Global Variable 
def Fun():   #------> Declaring function 
    a=30 #------> Local Variable
    print("Local Vaiable") 
    print("Value of a is ",a) #------->Printing 'a' As local Variable inside the function

print("Global Vaiable")   
print("Value of a is ",a)   #-------> printing 'a' as Global Variable

Fun()  #---------> Calling function

'''<------------------- Output ----------------->
Global Vaiable
Value of a is  20
Local Vaiable
Value of a is  30 '''


