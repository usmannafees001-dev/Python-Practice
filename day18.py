# string functions
# str.endwith(an)returns true if str ends with substr(an)otherwise false
str="usman"
print(str.endswith("an"))# it will return true
print(str.endswith("fu"))# it will return false
#str.capitalize it will capitalize the first word of str
str1="are you ok\nyes i am ok now"
print(str1.capitalize())# it will capitalize the only first world
print(",,,,,,,,,,,")
print(str1) # it will return the original value of str
print(",,,,,,,,,,,")
str1=str1.capitalize()# here it will capitalize the first word bcz we assign it in new varaible
print(str1.capitalize())
# str.replace means replace all the occurance of old characters of str with new
str2="usman nafees"
print(str2.replace("usman", "ahsan"))
# we can also replace the same type of alphabet from the sentence
str3="usman has won all the hackathones"
print(str3.replace("a","e"))
# str.find means returns first index of first occurer
str4="what type of hackathones you have won\n i worked on building real ai project e.t.c"
print(str4.find("worked"))
print(str4.find("t"))# it will return 3 index bcz we choose the single character
print(str4.find("what"))# it will return the first index of first occurer
print(str4.find("y"))# it will return 6 index bcz we choose the single character
print(str4.find("type"))# it will return the first index of first
print("find function ends here")
print(".......................") 
# str.colunt means it counts the occurence of substr
str5="in the world of programming the main thing is to solve the problem"
print(str5.count("i")) # it will tell that how many times i comes in the sentence
print(str5.count("ing"))
print(str5.count("solve"))
print("count functions ends here")
# some pratice questions are following 
# write a program to users first name and print its length
name=input("ENTER YOUR NAME: ")
print("LENGTH OF YOUR NAME IS:",len(name))
# WRITE A PROGRAM TO FIND THE OCCURENCE OF $ IN A STRING
income="i earn daily 5$ and monthly 150$ sometimes i earn 200$ "
print(income.count("$"))
# id card through input 
name=input("ENTER YOUR NAME: ")
roll_no=input("ENTER YOUR ROLL NO: ")
department=input("ENTER YOUR DEPARTMENT: ")
print(name.strip())
print(name.title())
print(roll_no.title())
print(roll_no.strip())
print(department.title())
print(department.strip())
print(f"{name} {roll_no} {department}")
# another method for student card is here
name=input("ENTER YOUR NAME: ").strip().title()
roll_no=input("ENTER YOUR ROLL NO: ").strip()
department=input("ENTER YOUR DEPARTMENT: ").strip().title()
print("---STUDENT CARD---")
print(f"student name: {name}")
print(f"roll no: {roll_no}")
print(f"department: {department}")
print(f"{name} {roll_no} {department}")