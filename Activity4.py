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
    opcio = int(input("CHOOSE AN OPTIONS --> "))
    if opcio == 1:
        DoHeadsAndTails()
    elif opcio == 2:
        DoRockPaperScissors()
    elif opcio == 0:
        flag = False
#END OF THE GAME. 
print("END OF THE GAME, THANK YOU FOR PLAYING!!!")