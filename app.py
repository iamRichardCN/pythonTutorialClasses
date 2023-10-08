name = input("please enter your name: ")
age  =int(input("How old are you: "))
yearsrange = 50 - age
if yearsrange>50:
    print("hello ", name, " its glad to see you.\nFun fact, do you know you are ", yearsrange, " years to 50?")
else:
    print("hello ", name, " its glad to see you.\nFun fact, do you know you are ", abs(yearsrange), " years more than 50?")
