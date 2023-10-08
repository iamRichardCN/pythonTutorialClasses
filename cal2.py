exp=[]
stopped = False

while not stopped:
    e =int(input("what is your expenditure(enter 0 when completed): "))
    if e!=0:
        exp.append(e)
    else:
        stopped = True
print("here is the list of your expense: ", exp)
print("total expense:", sum(exp))
print ("max expense: ", max(exp))
print ("minimum expense: ", min(exp) )