weight=71
height=1.75
bmi=weight/height**2
print(bmi)
if bmi<18.5:
    print("under weight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("over weight")
else:
    print("obese")            