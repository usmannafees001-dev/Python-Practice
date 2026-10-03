# # simple interst calculater
principal=float(input("ENTER THE PRINTCIPAL AMOUNT:"))
rate=float(input("ENTER THE RATE INTERST OF AMOUNT:"))
time=float(input("ENTER THE TIME :"))
simpleinterest=(principal*rate*time)/100
totalamount=principal+simpleinterest
print(simpleinterest)
print(totalamount)