def printing(m):
    for row in m:
        print(" ".join(row))

GB = [
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"]
]

tries = 6
done = True

secretword = "candy"

for i in range(tries):
    printing(GB)
    guess = input("Enter a 5-letter word: ").lower()
    
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue
    
    GB[i][0] = " " + guess[0] + " "
    GB[i][1] = " " + guess[1] + " "
    GB[i][2] = " " + guess[2] + " "
    GB[i][3] = " " + guess[3] + " "
    GB[i][4] = " " + guess[4] + " "

    if guess == secretword:
        print("You win!!!")
        done = False
        break

    for e in range(5):
        if guess[e] == secretword[e]:
            GB[i][e] = guess[e].upper()
        elif guess[e] in secretword:
            GB[i][e] = guess[e] + "*"

if done:
    print("You've used all your tries. The word was:", secretword)
