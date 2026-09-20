# break
# multiples of 3 [1 TO 50]=>21
for i in range(1,51):
    if(i==24):
       break
    if (i%3==0):
     print(i)

print("out of loop")

for i in range(1,90):
   if(i==9):
    continue
   if(i==12):
    continue
   if(i==15):
    continue
   if(i==18):
    continue
   if(i==21):
    continue
   if(i%3==0):
      print(i)
print("end of code here")

for i in range(10,0,-1):
   print(i)
print("new code is under this line")

i = 8
while i>=1:
  print(i*"8")
  i-=1
marks = [55,33,66,77]

print(marks, type(marks))
print(len(marks))
print(marks[0])
print(marks[0:3])
print(marks[-4:])
print(marks[:-4])
print(55 in marks)
print(333 in marks)
print("end of list here")
print("-----------")

print("printing the tuple")
marks = (66,33,77,98.68)
print(marks)
print(marks.index(66))
for score in marks:
 print(score)

print("end of tuple here")
print("..............")

# set is the unique items to collection

print("printing the set")
marks = {1,2,7,4,3,6,8,8,8,0,5}
print(len(marks) ,marks)
for score in marks:
 print(score)

print("end of set is here")
print(",,,,,,,,,,,,,,,,,,")

# dictionar{key => value}
marks = {"math":55,"english":66," ml": 76}
print(marks, type(marks))
marks["math"] =88
for key in (marks):
 print(key , marks[key])

print("end of dictionary here")
print("end ,,,,,,,,,,,,,,,,,,,")

# functions 
price = 34
new_price = price+(price*.56)
print(new_price)

# now if we want to calculate the sum than we can define the function like this
def any(a,b):
  print(a+b)
  print(a-b)
  print(a*b)
  print(a/b)

print("end of first function here")

def calc_gst(price):
  new_price = price+(price*(0.18))
  print(new_price)

calc_gst(20)
any(1,2)

print("end of code here")
print(",,,,,,,,,")
print("new code is here")

def calc_area(length,width):
    area = length*width
    return area

result = calc_area(4*5)
print(result)