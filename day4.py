# check for presence
name = ("usman nafees")
# here it also check whether the letter is capital or small
# it should be as it is in name as mentioned
print('s' in name)
new_name = ("USMAN NAFEES")
print('s' in new_name)
# if here we will check another word like x 
# it will not be printed bcz its does not exist
print('x' in name)
          # reserved keywords
# those words which we cannot use as a variable 
# True , False , while , for , in , continue , break


# practice exercise 2
# take the prices of three products
price1 = float(input("ENTER THE PRICE OF PRODUCT 1 :"))
price2 = float(input("ENTER THE PRICE OF PRODUCT 2 :"))
price3 = float(input("ENTER THE PRICE OF PRODUCT 3 :"))
total_bill = price1+price2+price3
average_bill = total_bill / 3
print("TOTAL BILL AMOUNT:" , total_bill)
print("AVERAGE PRICE:" , average_bill)
# another practice
super_hero_name = input("ENTER THE SUPER HERO NAME :")
starts_with_s = super_hero_name.lower().startswith("q")
print("DOES THE NAME STARTS WITH S OR s:" , starts_with_s)

