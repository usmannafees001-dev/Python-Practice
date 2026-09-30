# logical operators (and,or,not)
# and return true value if both conditions would be true
# otherwise return false

age=20
has_id=True
print(age>=18 and has_id)# it will return true value 
print(age<=18 and has_id)# it will return false value

# or operater return true value if one of them is true
# otherwise false (when both false)value
age=22
has_entrypass=True
print(age<=15 or has_entrypass)#it will return true value(both are true)
print(age>=18 or has_entrypass)# it will return also true(one of them is true)

# not operater reverse the conditions 
# false value return true value and true value return false
age=18
has_indentitycard=True
print(not age<=17)# it will return true value
print(not has_indentitycard)#it will return false value

a=34
b=55
print(not (a>b))#it will return true value
print(not (a<b))#it will return false value
print(not (b<a))#it will return true value