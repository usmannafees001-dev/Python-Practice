# this type of conversion called type casting
# it is that type of conversion is done by programer thats calld type casting
age = input("ENTER YOUR AGE: ")

new_age = int(age)+1 #this is #exlicit

print(new_age)
print(float(new_age))

#....
# this is type casting that programer doesnt do 
# it performs by the system
# it is done automatically 
print(1+2.45) # imlicit

# sum program=>a+b>=sum
a = int(input("ENTER a:"))
b = int(input("ENTER b:"))
sum = a+b
multiplication = a*b
substraction = a-b
division = a/b
print("sum:" , sum)
print("multiplication" ,multiplication)
print("substraction" , substraction)
print("division" , division)
# here we will see the upper and lower case
name = ("tony stark")
# it will print the all capital letters of tony stark
print(name.upper())
# it wil print the all small letters of usman nafees
new_name = ("USMAN NAFEES")
print(new_name.lower())
print(name.find("k")) # here we will see that how index will show the position of k
print(name.find("x"))# here we will see that x shows-1 bcz it doesnt exist 
# here you can see tha old vlue has been replaced by umais don
print(name.replace("tony stark" , "umais don"))
# if we want to replace ahsan with usman than we also can do it
print(new_name.replace("USMAN" , "ahsan"))
