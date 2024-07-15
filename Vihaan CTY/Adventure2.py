# ~~~Intro~~~
print("Welcome to the remote Airport! It is barely used and everyone speaks a different language. ")
print("You have gotten lost with all you have in your backack.")
print("Your goal is to escape before you encounter scary pigeons. (Hint:You need food, water and a weapon.)")
print("Survive and escpae fast, good luck!")
Backpack=[0,0,0]
def StatCheck(BP):
    print('In your backpack youll find:')
    if (BP[0]==0):
        print("You're out of food, find more or youll starve... ")
    else:
        print("You've found ",BP[0]," meals, though it doen't look quite good.")

    if (BP[1]==0):
        print("You're out of water, find more or youll die... ")
    else:
        print("You've found ",BP[1]," cups of water, though it doen't look clean.")
    
    if (BP[2]==0):
        print("You have no weapons, find more or you won't be able to defend yourself... ")
    else:
        print("You've found ",BP[2]," weapons.")
          #Try
        # print("You've found ",BP[3])

    
    #Except 

#FOUND WATER!
# Backpack[1]=Backpack[1]+100

# ~~~Options~~~
def optionsPrint(pervioushere):
    if (pervioushere[0]!=True):
        print("A. Get directions!")   
    if (pervioushere[1]!=True):
        print("B. Find food!")
    if (pervioushere[2]!=True):
        print("C. Explore!")
    if (pervioushere[3]!=True):
        print("D. Check Backpack.")
beenHere=[False,False,False,False]

done = False 

while done == False and (beenHere)!=[True,True,True,False]:
    optionsPrint(beenHere)
    user_choice = input("Which would you like to choose?(first letter should be UPPERcase)")

# ~~~Option A~~~
    if user_choice == "A":
        print("Pick your way to get direction (1. A tour guide, 2. A stranger, 3. A tour booth, 4. Guess.) Use Number")
        user_choice = input("Which direction do you chose?")
        if user_choice=='1':
            user_choice=input("You see a tour guide, he says go East, do you go East?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You found a maze that you got trapped in and you died.")
                done=True
                    #End Loop (Died)
            elif user_choice == "no":
                print("You walk forward, you go to find a safe place to sleep, because you were very very sleepy.")
                pass
                    #More Code (Lived)
        elif user_choice=="2":
            user_choice=input("You walk forward, talk in as much french, and you ask the stranger for a place to sleep, and they find you a bench, do you want to sleep?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You hurt your back and you died.")
                done=True
            #End Loop (Died)
            elif user_choice == "no":
                print("You progress on finding a better place to sleep.")
        elif user_choice == "3":
            user_choice=input("You ask a tour booth and they find you a hut, do you want to run?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You got struck by lightning.")
                done=True
            #End Loop (Died)
            elif user_choice== "no":
                print("you entered the cabin up and found a great place to sleep and a sword, which you throw in your backpack.")
                Backpack[2]=Backpack[2]+3
                pass
        elif user_choice == "4":
            user_choice=input("You found food, do you want to eat now?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You die, because they are expired.")
                done=True
            #End Loop (Died)
            elif user_choice == "no":
                print("You shove some expired apples into your backpack")
                Backpack[0]=Backpack[0]+3
                pass