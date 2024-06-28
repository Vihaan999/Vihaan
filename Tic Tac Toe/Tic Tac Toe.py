#~~~Variables~~~#
gameboard=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

endTheGame=False

#~~~Playing the Game~~~#
print("welcome to Tic-Tac-Toe")
while(endTheGame == False):

    for i in gameboard:
        print(i)
    

    playerInput= input("Where do you wanna go")
    print(playerInput)