from math import sqrt

avinp = input("Do you want  a average Calculator: ")
if avinp == "yes":
    print("If you less numbers put zero in")
    numnu = float(input("Choose Your Number: "))
    numnua = float(input("Choose Your Number: "))
    numnue = float(input("Choose Your Number: "))
    numnur = float(input("Choose Your Number: "))
    numnut = float(input("Choose Your Number: "))
    div = float(numnu + numnua + numnue + numnur + numnut)
    print(div/5)




if avinp == "no":
    inp = input("Do you want Square Root Calculator?:")
    if inp == "yes":
        num = float(input("Choose Your number: "))
        print(sqrt(num))
    if inp == "no":
        inpee = (input("Do you want highest Or Lowest Number Finder?: "))

    if inpee == "yes":
       minma = (input("Max Or Min: "))
    if minma == "Max":
        nums = float(input("Choose your first number"))
        numd = float(input("Choose your Sec number"))
        numf = float(input("Choose your Thir number"))
        numg = float(input("Choose your Forth number"))
        numh = float(input("Choose your Fith number"))
        print(max(nums, numd, numf, numg, numh))
    if minma == "Min":
        nums = float(input("Choose your first number"))
        numd = float(input("Choose your Sec number"))
        numf = float(input("Choose your Thir number"))
        numg = float(input("Choose your Forth number"))
        numh = float(input("Choose your Fith number"))
        print(min(nums, numd, numf, numg, numh))
    if inpee == "no":
        print("Mulitply = 1")
        print("Add = 2")
        print("Subtract = 3")
        print("Divide = 4")
        print("Power = 5")
        num1 = float(input("Enter your first number: "))
        op = (input("Enter your Operator: "))
        num2 = float(input("Choose Your Second Number: "))
        if op == "1":
            print(num1 * num2)  #
        elif op == "2":
            print(num1 + num2)
        elif op == "3":
            print(num1 - num2)
        elif op == "4":
            print(num1 / num2)
        elif op == "5":
            print(pow(num1, num2))
        else:
            print("Thats Invalid Dumbass")

