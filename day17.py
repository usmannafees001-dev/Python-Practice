# strings are data types 
# there are three type of string characters
# single qoute('') double qoute("") and triple qoute("""""")
str1='usman nafees'
str2="student of bs AI"
str3="""AI RESEARCHER"""
print(str1)
print(str2)
print(str3)
val1='he is taking his lectures" regularly'# we use diffrent type of string character 
# bcz sometime we use (any type of strig)in our sentence
# we also use escape sequence character
# means if we want our sentence in another line than we will use \n 
val2="where are you going man. \ni am going towards university"
# for tab space we will use \t
val3="yes i will go there \t but i have to take lecture first"
print(val1)
print(val2)
print(val3)
# basic operations in str 1= concatenation, 2=length of string
# in concatenation process values come closer to each other

firstname="AHSAN"
secondname="NAFEES"
print(firstname+secondname)
# in length of string it will tell the lenght of str that how much characters are there (in str)
print(len(firstname))
print(len(secondname))
# concatenation with length
name=firstname+" "+secondname# space in center will also be counted as a character
print(name)
print(len(name))# here it will show 12 characters are inside the str
# indexing = position number (means what will be the position of character)
# its start from 0 to 01234.....
num1="usman nafees"
print(num1)
# here we can access the character through number
print(num1[0])
print(num1[1])
print(num1[2])
print(num1[3])
print(num1[4])
print(num1[5])
# here we can access the number through character
print(num1.index("u"))
print(num1.index("s"))
print(num1.index("m"))
print(num1.index("a"))
print(num1.index("n"))
print(num1.index(" "))
# slicing = means accesing the parts of str
# in this concept starting index included but 
# ending index (type toh kiya jata hai lekin access nahi hota ) not included
num2="ARTIFICIAL INTELLIGENCE"
print(num2[0:10])
# we can also print the same thing like this 
print(num2[:10])
print(num2[11:23])
print(num2[0:23])
# we can also print the whole str like this
print(num2[0:])
# if we want to go towards last index than we can type the length
print(num2[11:len(num2)])
# we also can count our index backward (means from last word to initial)
# and it starts from -1(last word)
print(num2[-23:-1])
print(num2[-23:-13])