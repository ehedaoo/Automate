import random

randnum = int(random.randint(1, 20))

for i in range(1, 10):
    guess = int(input("Think of the number I'm thinking of: "))
    if guess < randnum:
        print("Low")
        continue
    elif guess > randnum:
        print("High")
        continue
    else:
        break

if guess == randnum:
    print("You took " + str(i) + " times to make the correct guess.")
else:
    print("The number I thought of was " + str(randnum))