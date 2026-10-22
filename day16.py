# two types of conversion
# type casting = means manually convert the value
a=int("4") # here str value converted into the integer
b=7
sum=a+b
print(sum)

# type conversion = means this conversion done automatically 
a=8
b=6.9 # float value
sum=a+b  # in this method we will see that int value converted in the float value 
                        #(bcz the float value is superior)
print(sum)
# type casting
a=str(78)
b=str(876)
print(type(a))
print(type(b))
print(a+b)

# input = statment is used to accept the values (using keyboard) from user
input("ENTER YOUR NAME: ")
# WE CAN ALSO STORE THE INPUT VALUE IN VARIABLE
name=input("enter your name: ")
print("how are you: ",name)