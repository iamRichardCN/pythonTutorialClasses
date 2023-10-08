exp= -1
total = 0
maxexp = 0
minexp = 0

while exp!=0:
    exp= int(input("what is your expenditure(enter 0 when completed): "))
    if exp == 0:
        break  
    total = total + exp
    if exp>maxexp:
        maxexp=exp
    if exp<maxexp:
        minexp=exp
          
print("your total expenditure is ", total)
print("your Maximum expense is ", maxexp)
print("your Maximum expense is ", minexp)