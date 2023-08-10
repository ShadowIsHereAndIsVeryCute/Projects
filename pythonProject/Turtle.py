rar = (input("How many engines do you need.write I for each one: "))

if rar <= "Yes":
    for rar in  rar:
        num1 = float(input("Litre amount: "))

        if num1 >= 3:
            print("500")

        elif num1 >= 2:
            print("300")
        elif num1 >= 1:
            print("100")
        elif num1 >= 0:
            print("You dont have road tax")


elif rar == "No":
    print("No Tax Found")

else:
    print("Thats not valid")

