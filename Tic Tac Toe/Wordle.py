def getUserIn(GB):


 return GB

def printing(m):
    for i in m:
        print(i)
       
        
GB=[
    ["|_|","|_|","|_|","|_|","|_|"],

    ["|_|","|_|","|_|","|_|","|_|"],

    ["|_|","|_|","|_|","|_|","|_|"],

    ["|_|","|_|","|_|","|_|","|_|"],

    ["|_|","|_|","|_|","|_|","|_|"],

    ["|_|","|_|","|_|","|_|","|_|"]



]
tries=6
done=True

secretword="pzazz"

    #format end
for i in range(0,6):
        printing(GB)
        guess=input("Enter a 5 letter word. ")
        GB[i][0]=" "+guess[0]+"" 
        GB[i][1]=" "+guess[1]+""
        GB[i][2]=" "+guess[2]+""
        GB[i][3]=" "+guess[3]+""
        GB[i][4]=" "+guess[4]+""
       
    
        if guess==secretword:
            print("You win!!!")
            done==False
            break

        elif guess!=secretword:
            for e in range(0,5):
                if guess[e]==secretword[e]:
                    GB[i][e]=guess[i].upper()
                elif guess[e] in secretword:
                    GB[i][e]=guess[e]+"*"

    