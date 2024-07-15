def factorial(inputlist):
    for i in inputlist:
        print (i)

x=1
y=input("enter input")
y=int(y)
for i in range(y,0,-1):
    x=x*i
    print(x)