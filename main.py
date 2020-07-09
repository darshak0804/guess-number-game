import random

def total():
    print(f"Overall Score is :\n")
    if count<count2:
        print("player 1 is win")
    elif count>count2:
        print("player 2 is win")
    else:
        print("the GAME")
        return
a = int(input("Enter the value of A"))
b = int(input("enter the value of B"))

count = 0
count2 = 0


answer = random.choice(range(a,b))

while True:
    print("Player one turn:")
    val = int(input("enter any number"))
    count = count + 1
    if val<answer:
        print("Enter Bigger Number")
        print(f"You Take {count}Chance")

    elif val>answer:
        print("Enter Smaller Number")
        print(f"You Take {count}Chance")
    elif val == answer:
        print("Player 1 Guess Correct Answer")
        print(f"You take {count} chance to guess number")
        print(answer)
        break

    else:
        print("Something went To Wrong")

while True:
    print("player 2 Turn\n")
    val2 = int(input("enter the any number"))
    count2 = count2 + 1
    if val2<answer:
        print("Enter Bigger Number")
        print(f"You take {count2}Chance")


    elif val2>answer:
        print("Enter Smaller Number")
        print(f"You take {count2} Chance")

    elif val2 == answer:
        print("You have Correct answer")
        print(f" You take{count2}  chance for the guess number")
        break

    else:
        print("Something went to wrong")

total()

print("Game Over")

