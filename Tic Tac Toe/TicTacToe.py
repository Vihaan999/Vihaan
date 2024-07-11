def fullprint(gameboard):
    for i in range(0,len(gameboard)):
        for k in range(0,len(gameboard[i])):
            if k == len(gameboard[i])-1:
                print(gameboard[i][k])
            else: 
                print(gameboard[i][k], end=" ")
#~~~Variables~~~#
player="X"

gameboard=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

endTheGame=False
Z=0
#~~~Playing the Game~~~#
print("welcome to Tic-Tac-Toe")
while(endTheGame == False):
    if player=="X":
        player="O"
    elif player=="O":
        player="X"
    fullprint(gameboard)
    Y= int(input("Which row? (1-3)"))-1
        
    X= int(input("Which column? (1-3)"))-1


    if Y>=4:
        print("You cant move there,your turn get skipped loser.")
        continue
    elif Y<=-1:
        print("You cant move there,your turn get skipped loser.")
        continue

    elif X>=4:
        print("You cant move there,your turn get skipped loser.")
        continue
    elif X<=-1:
        print("You cant move there,your turn get skipped loser.")
        continue
    else:
        gameboard[Y][X]=player
        Z+=1
        
    if gameboard[0][0]==gameboard[0][1]==gameboard[0][2] != 0:
        print ("You win!!!:)")
        endTheGame == True
    elif gameboard[1][0]==gameboard[1][1]==gameboard[1][2] != 0:
        print ("You win!!!:)")
        endTheGame == True
    elif gameboard[2][0]==gameboard[2][1]==gameboard[2][2] != 0:
        print ("You win!!!:)")
        endTheGame == True

    elif gameboard[0][0]==gameboard[1][0]==gameboard[2][0] != 0:
        print ("You win!!!:)")
        endTheGame == True
    
    elif gameboard[0][1]==gameboard[1][1]==gameboard[2][1] != 0:
        print ("You win!!!:)")
        endTheGame == True
    
    elif gameboard[0][2]==gameboard[1][2]==gameboard[2][2] != 0:
        print ("You win!!!:)")
        endTheGame == True
    

    elif gameboard[0][0]==gameboard[1][1]==gameboard[2][2] != 0:
        print ("You win!!!:)")
        endTheGame == True
    elif gameboard[0][2]==gameboard[1][1]==gameboard[2][0] != 0:
        print ("You win!!! :)")
        endTheGame == True

    elif Z==9 :
        print("you tie")
        endTheGame == True

    
    
    
    