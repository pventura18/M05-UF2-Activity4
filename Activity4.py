import random

#Pol Ventura
def DoHeadsAndTails():
    print("In this game you choose HEADS or TAILS and the computer tosses a virtual coin.")
    selection = input("Now choose: HEADS or TAILS? --> ")
    coin = random.randint(0,1)
    if coin == 0 and selection == "HEADS":
        print("CONGRATULATIONS!!! It is HEADS!!!")
    elif coin == 1 and selection == "TAILS":
        print("CONGRATULATIONS!!! It is TAILS!!!")
    elif coin == 1 and selection == "HEADS":
        print("SORRY!!! It was TAILS!!!")
    elif coin == 0 and selection == "TAILS":
        print("SORRY!!! It is HEADS!!!")
    else:
        print("YOU DIDN'T CHOOSE HEADS OR TAILS! WHAT???")
#Pol Besalú

def DoRockPaperScissors():

    def play():
        user = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return 'It\'s a tie!'

        if is_win(user, computer):
            return 'You won!'

        return 'You lost!'

    def is_win(player, opponent):
        # return true if player wins
        # r > s, s > p, p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
    print(play())
    
#Martí Roura
def DoEvensAndOdds(): 
    print("In this game you choose EVENS or ODDS.")
    print("Then you and the computer choose a number from 0 to 5.")
    print("The winner is based on the sum of those numbers.")
    
    #if the number given is not 1 or 2 we ask it again
    playerOption = AskEvensAndOddsOption()
    while (playerOption != 1 and playerOption != 2):
        playerOption = AskEvensAndOddsOption()
    
    #we ask a number between 0 and 5, if it's not valid we ask it again
    playerNumber = AskEvensAndOddsNumber()
    while (playerNumber < 0 or playerNumber > 5):
        playerNumber = AskEvensAndOddsNumber()
    
    #we compute the computer's number and if the result is even or odd
    computerNumber = random.randint(0, 5)
    resultNumber = playerNumber + computerNumber
    isEven = resultNumber % 2 == 0

    #we print the final result
    print(f"The result is {playerNumber} + {computerNumber} = {resultNumber}")
    if playerOption == 1:
        if isEven:
            print("Congratulations you WON!")
        else:
            print("I'm sorry you LOST :(")
    if playerOption == 2:
        if isEven:
            print("I'm sorry you LOST :(")
        else:
            print("Congratulations you WON!")

#we ask for a number that represents EVEN or ODDS as the user option
def AskEvensAndOddsOption():
    return int(input("Now choose: \nPress 1 for EVENS \nPress 2 for ODDS\n"))

#we ask for a number from 0 to 5
def AskEvensAndOddsNumber():
    return int(input("Now choose a number from 0 to 5\n"))

opcio = 0
flag = True

while flag == True:
    
    print("""
    WHAT DO YOU WANT TO PLAY?
    
    1) Heads and Tails
    2) Rock, Paper, Scissors
    3) Evens and Odds
    4) Memory Test
    0) EXIT
    """)
    
    opcio = int(input("CHOOSE AN OPTION --> "))
    if opcio == 1:
        DoHeadsAndTails()
    elif opcio == 2:
        DoRockPaperScissors()
    elif opcio == 3:
        DoEvensAndOdds()
    elif opcio == 0:
        flag = False
        
print("END OF THE GAME, THANK YOU FOR PLAYING!!!")