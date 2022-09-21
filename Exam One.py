import random
print("Winner and Losers - Human is Even, Computer is Odd")

human = 0
computer = 0
round = 1

for round in range(1, 6):
    print("Round: {}".format(round))
    humanguess = int(input("Enter your guess: "))
    computerguess = random.randint(1,5)
    
    if humanguess > 5:
        humanguess = 5

    sumEven = False if (computerguess + humanguess)%2 else True

    if sumEven:
        human += 1
    else:
        computer += 1
    
    print("Human Guess: {} - Computer Guess: {}".format(humanguess, computerguess))

    if sumEven:
        print("Sum is Even")
    else:
        print("Sum is Odd")
    
    print("Human Score: {} - Computer Score: {}".format(human,computer))

    round += 1
    print()

if human > computer:
    print("Human Wins")
else:
    print("Computer Wins")
