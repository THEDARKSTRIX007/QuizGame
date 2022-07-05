print("Welcome to the Quiz Game")

playing = input("Do you wanna play?\n")

if playing.lower() != "yes":
    quit()

print("Let's Play" )

score = 0

answer = input("What does CPU stands for?\n")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does GPU stands for?\n")
if answer.lower() == "Graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does WHO stands for?\n")
if answer.lower() == "World Health Orgnisation":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does IPL stands for?\n")
if answer.lower() == "Indian Premier League":
    print("Correct")
    score += 1
else:
    print("Incorrect")


print("You got " + str(score) + " Questions Right!")

print("You got " + str((score/4)*100) + "%.")