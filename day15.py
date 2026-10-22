# # simple interst calculater
principal=float(input("ENTER THE PRINTCIPAL AMOUNT:"))
rate=float(input("ENTER THE RATE INTERST OF AMOUNT:"))
time=float(input("ENTER THE TIME :"))
simpleinterest=(principal*rate*time)/100
totalamount=principal+simpleinterest
print(simpleinterest)
print(totalamount)

#way 1 of basic calculater
a=float(input("ENTER THE FIRST NUMBER:"))
b=float(input("ENTER THE SECOND NUBMER:"))

print("ADDITION:" ,a+b)
print("SUBSTRACTION:" ,a-b)
print("MULTIPLICATION:" ,a*b)
print("DIVISION:" ,a/b)

# way 2 caculater by using conditions if/elif/else

a=float(input("ENTER THE FIRST NUBMER:"))
b=float(input("ENTER THE SECOND NUMBER:"))
op=input("ENTER THE OPERATER (+,-,/,*,%):")

if op=="+":
    print("RESULT:",a+b)
elif op=="-":
    print("RESULT:",a-b)
elif op=="*":
    print("RESULT:",a*b)
elif op=="/":
    if b==0:
        print("error cannot divide by zero")
    else:
        print("RESULT:",a/b)
else:
    print("invavlid op")

# way 3 to make the calculater by using the functions 

def addition(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
x=float(input("ENTER THE FIRST NUMBER:"))
y=float(input("ENTER THE SECOND NUMBER:"))
op=input("ENTER THE OPERATERS(+,-,/,*):")
if op=="+":
    print(addition(x,y))
elif op=="-":
    print(substraction(x,y))
elif op=="/":
    print(division(x,y))
else:
    print(multiplication(x,y))

