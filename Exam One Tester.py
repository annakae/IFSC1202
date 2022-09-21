# module imported to generate random number
import random

''' QUESTION 1 ''' 
# title of the game
print("Winners and Losers")
# initialize human and computer points to 0
human_point = 0
computer_point = 0
# initialize round to 1
round = 1

# run this loop till the round is less than 6

''' QUESTION 2 '''
for round in range(1,6):
    
    ''' QUESTION 3 '''
    # displaying round number
    print("Round", round)
    
    ''' QUESTION 4 '''
    # prompt for human to enter the number
    human_input = int(input("Enter a number between 1 and 5: "))
    
    ''' QUESTION 5 '''
    # generate a random integer in the inclusive range of 1 and 5
    computer_input = random.randint(1, 5)
    if human_input > 5:
        human_input = 5

    # A % 2 will be 0 if A is even and 1 if A is odd
    # therefore if the sum of both the input is odd then
    # boolean sumIsEven is initialized to false as then it's not even.
    # and if the sum is even then it is initialized to true.

    sumIsEven = False if (computer_input + human_input)%2 else True
    
    ''' QUESTION 6 '''
    # if sum is even then human gets the point
    if sumIsEven:
       human_point += 1
    # if sum is odd then computer gets the point
    else:
        computer_point += 1 

    ''' QUESTION 7 '''
    # displaying the human and computer inputs
    print("human guess: ", human_input)
    print("computer guess: ", computer_input)

    ''' QUESTION 8 '''
    # displaying whether the sum is even or odd
    if sumIsEven:
        print("Sum is Even")
    else:
        print("Sum is Odd")


    ''' QUESTION 9 '''
    # displaying the human and computer scores
    print(f"human score after round {round} => ", human_point)
    print(f"computer score after round {round} => ", computer_point)

    round += 1
    print()

''' QUESTION 10 '''
# After 5 rounds .....
# if the human score is greater than the computer score then the human wins the game
if human_point > computer_point:
    print("Human Wins")
# if the computer score is greater than the human score then the computer wins the game
else:
    print("Computer Wins")