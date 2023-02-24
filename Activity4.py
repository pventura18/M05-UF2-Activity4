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

#Martí Roura






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
    
    opcio = int(input("CHOOSE AN OPTIONS --> "))
    if opcio == 1:
        DoHeadsAndTails()
    elif opcio == 0:
        flag = False
        
print("END OF THE GAME, THANK YOU FOR PLAYING!!!")