is_male = True
is_tall =False

if is_male and is_tall:
    print("You are a Tall male")
elif is_male and not (is_tall):
    print("you are a guy but your short")
elif not(is_male) and is_tall:
    print("YOur a tall woman")
else:
    print("you neither male nor tall")

