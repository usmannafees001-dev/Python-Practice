# conditional statments 
age = 17
if age >= 18:
    print("you are an adult")
    print("you can drive / vote ")
    print("you can participate in riding / you can do whatever you want to do")
# here it will print only that block of code which accurately satisfy its condition
elif age < 18:
    print("you cant do these things like / vote /drive / riding")
    print("you are restricted")
print("end of code :")
print(".........")

marks = 88
# here it will print (a) bcz its satisfying its condition 1
if marks >=80:
   print("A")
elif marks < 80 and marks >= 60:
    print("B")
elif marks < 60:
    print("C")

print(".........")

marks = 70
# here it will print (b) bcz its satisifying the condition 2
if marks >=80:
   print("A")
elif marks < 80 and marks >= 60:
    print("B")
elif marks < 60:
    print("C")

print(".........")

marks = 55
# here it will print (c) bcz its satisifying the condition 2
if marks >=80:
   print("A")
elif marks < 80 and marks >= 60:
    print("B")
elif marks < 60:
    print("C")