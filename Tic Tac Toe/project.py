# ~~~Intro~~~
print("Welcome to the Woods!")
print("You have gotten lost with all you have in your backack.")
print("Your goal is to escape before you encounter scary animals. (Hint:You need food, water and a weapon.)")
print("Survive and escpae fast, good luck!")
Backpack=[0,0,0]
def StatCheck(BP):
    print('\nIn your backpack youll find:')
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
        print("A. Hunt for food.")   
    if (pervioushere[1]!=True):
        print("B. Find shelter and make a camp.")
    if (pervioushere[2]!=True):
        print("C. Explore!")
    if (pervioushere[3]!=True):
        print("D. Check Backpack.")
    
done = False 
beenHere=[False,False,False,False]


while done == False and (beenHere)!=[True,True,True,False]:
    optionsPrint(beenHere)
    user_choice = input("Which would you like to choose?(first letter should be UPPERcase) ")
# ~~~Option A~~~
    if user_choice == "A":
        print("Pick your direction (North, South, East, or West.")
        user_choice = input("Which direction do you chose)(first letter should be UPPERcase)")
        if user_choice=='North':
            user_choice=input("You feel your tummy wumble, should you go hunting?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You found killed a deer, but his family came and ended you and you have died.")
                done=True
                    #End Loop (Died)
            elif user_choice == "no":
                print("You walk forward, you go to find a safe place to sweepy, because you were werry werry sweepy.")
                pass
                    #More Code (Lived)
        elif user_choice=="South":
            user_choice=input("You have discovered a lake, do you want to swim?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You drowned.")
                done=True
            #End Loop (Died)
            elif user_choice == "no":
                print("you dip your toes in the water and enjoy the sites")
        elif user_choice == "East":
            user_choice=input("You found a Cabin, do you want to run?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You fell off a cliff and got eaten by wolves.")
            elif user_choice== "no":
                print("you entered the cabin up and found a great place to sweep and a bow and aarow, which you throw in your backpack.")
                Backpack[2]=Backpack[2]+3
                pass
        elif user_choice == "West":
            user_choice=input("You found food, do you want to eat now?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You die, because they are rotten.")
                done=True
            #End Loop (Died)
            elif user_choice == "no":
                print('You shove a few rotting slabs of meat into your backpack')
                Backpack[0]=Backpack[0]+3
                pass
# ~~~Option B~~~
    elif user_choice == "B":
        print("Pick your choice(1. Get trees, 2. Go deeper in woods 3.Sleep on ground)")
        user_choice = input("Which option do you chose)(Use the number)")
        if user_choice=='1':
            user_choice=input("You find a dead tree on the ground, do you use it? (first letter should be lowercase)")
            if user_choice == "yes":
                print("Your shelter got attacked by a bear and you died.")
                done=True
                    #End Loop (Died)
            elif user_choice == "no":
                print("You get struck by lightning and you died.")
                done=True
                    #End Loop (Died)
        elif user_choice=="2":
            user_choice=input("You have discovered an asleep pack of wolves, do you want to run away?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You get chased and but survive.")
            elif user_choice == "no":
                print("You hide and live to mew another day, or so you think. They came back and killed you.")
                done=True
            #End Loop (Died)
        elif user_choice == "3":
            user_choice=input("You see a muddy area, do you sleep there?(first letter should be lowercase)")
            if user_choice == "yes":
                print("you get slurped into the ground")
                done=True
            #End Loop (Died)
            elif user_choice== "no":
                print("You get cold at night but live to mew another day.")
# ~~~Option C~~~
    elif user_choice == "C":
        print("Pick your area to explore (1. Lake, 2. TreeHouse, 3. Cave.")
        user_choice = input("Which direction do you chose)(Use number)")
        if user_choice=='1':
            user_choice=input("You see a lake, do you want to make a raft and swim? (first letter should be lowercase)")
            if user_choice == "yes":
                print("You found a raft, but it sunk as you were paddling and you have died.")
                done=True
                    #End Loop (Died)
            elif user_choice == "no":
                print("You sit and admire the amazing sites of the woods and collected water in bottles and throw them into your bag.")
                Backpack[1]=Backpack[1]+5
                pass
                    #More Code (Lived)
        elif user_choice=="2":
            user_choice=input("You have discovered a treehouse, do you want to enter?)")
            if user_choice == "yes":
                print("You tripped on a stick and fell out, but you survived, because it was only 1.5 feet above ground.")
            elif user_choice == "no":
                print("the gnomes in the treehouse shot you.")
                done=True
            #End Loop (Died)
        elif user_choice == "3":
            user_choice=input("You found a Cave, do you want to enter?(first letter should be lowercase)")
            if user_choice == "yes":
                print("You entered the cave and found the wolves you have to kill to escape.")
                beenHere=[True,True,True,False]
                done=True
                break
            elif user_choice== "no":
               pass
    elif user_choice=='D':
        StatCheck(Backpack)
        print("You may live to mew another day ")
donefinalpart=False
while donefinalpart==False:
  
            #End Loop (Died)
    if Backpack==[3,5,3]:
        print("the wolves attacked the bag and not you, YOU WON!!!")
        donefinalpart=True
  

