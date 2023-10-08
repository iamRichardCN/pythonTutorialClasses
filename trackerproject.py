from datetime import date
import csv

dt= date.today()
dt= dt.strftime("%d/%m/%y")

#print(dt)

filename = "test.csv"

exp=[]
stopped = False

with open(filename, 'a', newline="") as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp=int(input("what is your expense today(cost)? (type 0 to stop):  "))
        if xp==0:
            stopped=True
        else:
            name=input("what is this expense for :")
            csvwriter.writerow([dt, xp, name])
            exp.append(xp)
file.close()
print("your expense today are: ", exp)
print("your total expenses are ", sum(exp))
