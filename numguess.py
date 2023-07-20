import random
randomnum=random.randint(0,25)
max_attempts=3
def guess():
    return int(input("Enter your number you guessed between 0 to 25: "))
for attempt in range (1,max_attempts+1):
    num = guess()
    if attempt==max_attempts:
        print("Better Luck Next time, The correct number is", randomnum)
    elif num==randomnum:
        print("Muthey! Nee Dhamla")
    elif num > 25 or num < 0:
        print("Try numbers between 0 to 50")
    elif num > randomnum:
        print("Try out something small")
    elif num < randomnum:
        print("Try out something big")
    