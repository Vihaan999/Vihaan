# ~~~Board~~~
Gameb=[
["#","#","#","#","#","#","#","#","#","#","#","#"],
["#","&"," "," "," "," ","*","#","#","#","#","#"],                 
["#"," "," ","#","#"," "," "," "," "," "," ","#"],
["#","*"," "," ","#","#","#","#","#","*"," ","#"],
["#","#","#"," "," "," "," "," ","*","#"," ","#"],
["#"," "," "," ","#","#","#","#","#","*"," ","#"],
["#","#","#"," "," "," "," "," "," "," ","E","#"],
["#","#","#","#","#","#","#","#","#","#","#","#"]]
x=1
y=1
c=0
done = False 
while done == False:
    for i in range(0,len(Gameb)):
        for k in range(0,len(Gameb[i])):
            if k == len(Gameb[i])-1:
                print(Gameb[i][k])
            else: 
                print(Gameb[i][k], end=" ")
# ~~~Movement
    Gameb[y][x] =" "
    user_input=input("Use W,A,S,D to navigate the maze. You need to collect all 5 coins.")
    if user_input == "W" or user_input == "w":
        if Gameb[y - 1][x] == " " or Gameb[y - 1][x] == "E" or Gameb[y - 1][x] == "*":
            y -= 1
    elif user_input == "A" or user_input == "a":
        if Gameb[y][x - 1] == " " or Gameb[y][x - 1] == "E" or Gameb[y][x - 1] == "*":
            x -= 1
    elif user_input == "S" or user_input == "s" :
        if Gameb[y + 1][x] == " " or Gameb[y + 1][x] == "E" or Gameb[y + 1][x] == "*": 
            y += 1
    elif user_input == "D" or user_input == "d":
        if Gameb[y][x + 1] == " " or Gameb[y][x + 1] == "E" or Gameb[y][x + 1] == "*":
            x += 1
    
    Gameb[y][x] = "&"
    if Gameb[6][10]=="&" and c>=5:
        print("You Win!!!")
        done = True
    elif Gameb[6][10]=="&" and c<5:
        print("you lose, loser")
        done = True
# ~~~ Collecting Coins~~~
    if Gameb[3][1]=="&":
        print("You got a coin!!!")
        c+=1
    Gameb[y][x] = "&"
    if Gameb[1][6]=="&":
        print("You got a coin!!!")
        c+=1
    Gameb[y][x] = "&"
    if Gameb[3][9]=="&":
        print("You got a coin!!!")
        c+=1
    Gameb[y][x] = "&"
    if Gameb[4][8]=="&":
        print("You got a coin!!!")
        c+=1
    Gameb[y][x] = "&"
    if Gameb[5][9]=="&":
        print("You got a coin!!!")
        c+=1