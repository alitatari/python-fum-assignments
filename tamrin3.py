import random
print("hello,welcom players")
while True :
    
    playerDecision = int(input("choose a Option :\n1) Start Game 1 Dice\n2) Exit\n"))
    if playerDecision == 1:
    
        for player in range(1):
            result = random.randint(1,6)
            print("Result for is:" ,  result )
        if result == 6:
            print("do bareh jayzeh tas ro  bandaz")
        
    else:
        break