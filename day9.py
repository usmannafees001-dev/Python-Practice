# range / loops = while loop and for loop
    # while loop
# counter 1,2,3,4,5
# while loop performs a function untill conditiom becomes true
i = 1
while i <=5:
    print(i *"i")# 5 times i would be printed
    i +=1
print("end of code:")
print("......")

# now (for) loop here code perform a function to the known numbers of time 
nums = range(5) # 0 to 4 would be printed
for i in nums:
    print(i)

print("end of code")

# nums = range(6) # 0 to 5 would be printed
for i in range(1,6):
    print(i)
# if we want to print the value for 100 times than we should enter 101 in command line
for i in range(1,101):
    print(i)
# now if we want to print the even numbers from 2 to onword
i = 10
for i in range(0,12,2):
     print(i)
# if we want to do the same thing than another method of doing this is 

print("end of code here")
i = 11
for i in range(1,11):
    if i%2==0:
        print(i)