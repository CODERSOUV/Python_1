import random
r = [1, 2, 3]
print("----Rock Paper Scissors---")
print("For rock, press 1\nFor paper, press 2\nFor scissors, press 3")

choose = int(input("What will you choose?"))

computer_choice = random.choice(r)

if choose == computer_choice:
    print("Draw match")
elif choose == 1 and computer_choice == 2:
    print("You lost!")
elif choose == 1 and computer_choice == 3:
    print("You win!")
elif choose == 2 and computer_choice == 1:
    print("You win!")
elif choose == 2 and computer_choice == 3:
    print("You lost!")
elif choose == 3 and computer_choice == 1:
    print("You lost!")
elif choose == 3 and computer_choice == 2:
    print("You win!")
else:
    print("You entered a wrong choice.")

print("Computer's choice:", computer_choice)
