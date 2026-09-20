# today we will build calculater that performs the following calculations
# '''a+b / a-b / a%b / a*b / a**b / a/b'''

a = float(input("ENTER THE FIRST NUMBER:"))
b = float(input("ENTER THE SECOND NUMBER:"))
op = input("ENTER THE OP(+ ,- ,* ,/ ,% ,**):")

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
elif op=='%':
    print(a%b)
elif op=='**':
    print(a**b)
else:
    print("INVALID OPERATIONS")