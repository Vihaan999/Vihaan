# ~~~GameBoard~~~

def fullprint(Gameb):
    for i in range(0,len(Gameb)):
        for k in range(0,len(Gameb[i])):
            if k == len(Gameb[i])-1:
                print(Gameb[i][k])
            else: 
                print(Gameb[i][k], end=" ")

player="#"

Gameb=[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
    ]

fullprint(Gameb)
endTheGame=False

# ~~~Code~~~
print("welcome to Connect4")
while(endTheGame == False):


    if player=="#":
        player="$"
    elif player=="$":
        player="#"
    

    Y= int(input("Which column? (1-7)"))-1


    if Y>=8:
        print("You cant move there,your turn get skipped loser.")
        continue
    if Y<=-1:
        print("You cant move there,your turn get skipped loser.")
        continue

    for t in reversed(range(0,len(Gameb))):
    
        if Gameb[t][Y]==0:
            Gameb[t][Y]=player
            break


        
    for i in range(0,9):    
        for k in range(0,7):
            try:    
                if Gameb[i][k]==Gameb[i][k+1]==Gameb[i][k+2]==Gameb[i][k+3]!=0 or Gameb[i][k]==Gameb[i+1][k]==Gameb[i+2][k]==Gameb[i+3][k]!=0 or Gameb[i][k]==Gameb[i+1][k+1]==Gameb[i+2][k+2]==Gameb[i+3][k+3]!=0 or (Gameb[i][k]==Gameb[i+1][k+1]==Gameb[i+2][k+2]==Gameb[i+3][k+3]!=0) or (Gameb[i][k]==Gameb[i+1][k-1]==Gameb[i+2][k-2]==Gameb[i+3][k-3]!=0): 
                     print ("You win!!!:)")
                     endTheGame=True
                     break
            except(IndexError):
                pass
    
    fullprint(Gameb)



