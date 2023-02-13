#Pol Ventura
def DoHeadsAndTails():
    

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