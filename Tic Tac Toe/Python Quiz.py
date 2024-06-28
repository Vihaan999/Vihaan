correct=0

def ask(question, answer):
    q = input(question)
    if q == answer:
        print("correct:)")
        return 1
    else: 
        print("incorrect:(")
        return 0

correct += ask("What is 10*10", "100")
correct += ask("What is 100/10", "10")
correct += ask("What is my name", "Vihaan")
correct += ask("What is How old am I", "12")
correct += ask("What is What is my favorite video game", "Fortnite")

print("You got "+str(correct)+" out of 5 correct!")