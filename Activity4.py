import random

#Pol Ventura
#This is a function to play Heads and Tails with the console.
def DoHeadsAndTails():
    #The machine asks you to choose HEADS or TAILS.
    print("In this game you choose HEADS or TAILS and the computer tosses a virtual coin.")
    selection = input("Now choose: HEADS or TAILS? --> ")
    
    #It generates a random number which is 1 or 0.
    coin = random.randint(0,1)
    
    #Depending on the number generated and your option, you win or you lose. If machine chooses 0 it is HEADS and if it chooses 1 it is TAILS.
    if coin == 0 and selection == "HEADS":
        print("CONGRATULATIONS!!! It is HEADS!!!")
    elif coin == 1 and selection == "TAILS":
        print("CONGRATULATIONS!!! It is TAILS!!!")
    elif coin == 1 and selection == "HEADS":
        print("SORRY!!! It was TAILS!!!")
    elif coin == 0 and selection == "TAILS":
        print("SORRY!!! It is HEADS!!!")
    #It is an alternative text for when you don't choose between HEAD and TAILS.
    else:
        print("YOU DIDN'T CHOOSE HEADS OR TAILS! WHAT???")
        
#Pol Besalú

def DoRockPaperScissors():

    def play():
        #It asks you to enter a character r, p or s to choose between rock, paper and scissors.
        user = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
        #The computer chooses randomly between r, p and s.
        computer = random.choice(['r', 'p', 's'])

        #This option is the tie if the two have the same selection.
        if user == computer:
            return 'It\'s a tie!'

        #This option if the user won the computer
        if is_win(user, computer):
            return 'You won!'

        #And finally the option if the user loses against the computer.
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
    #IT PRINTS A MENU WITH DIFFERENTS OPTIONS TO PLAY.
    print("""
    WHAT DO YOU WANT TO PLAY?
    
    1) Heads and Tails
    2) Rock, Paper, Scissors
    3) Evens and Odds
    0) EXIT
    """)
    
    #IT ASKS YOU TO ENTER AN OPTION OF THE MENU.
    opcio = int(input("CHOOSE AN OPTION --> "))
    if opcio == 1:
        DoHeadsAndTails()
    elif opcio == 2:
        DoRockPaperScissors()
    elif opcio == 3:
        DoEvensAndOdds()
    elif opcio == 0:
        flag = False
#END OF THE GAME. 
print("END OF THE GAME, THANK YOU FOR PLAYING!!!")