sw = "Monkey"
guess: = ""
guess_count = 0
guess_limit = 3
Out_Of_Guesses = False

while guess != sw and not (Out_Of_Guesses):
    if guess_count < guess_limit:
     guess = input("Enter Guess: ")
    guess_count += 1
else:
    Out_Of_Guesses = True
if Out_Of_Guesses
    print("Out of guesses, YOU LOSE!!")
print("You win")
