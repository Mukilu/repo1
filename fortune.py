import random
play = "yes"
print("Welcome to Future Predictor")
print("Enter your favorite colour and number to know about your future")
while play=="yes":
    color=input("Enter your favorite colour [Red, Green, Blue, Yellow]")
    if color=="Red" or color=="Green":
        number=int(input("Enter number like 1,4,7,9 : "))
        if number==1:
            print("You're going to be a millionaire")
        elif number==4:
            print("You're going to be a billionaire")
        elif number==7:
            print("You're going to be a trillionaire")
        elif number==9:
            print("You're going to be a quadrillionaire")
        else:
            print("Only numbers 1,4,7,9 are allowed ")
    elif color=="Blue" or color=="Yellow":
        number=int(input("Enter number like 2,3,5,8 : "))
        if number==3:
            print("You're going to be a MLA")
        elif number==8:
            print("You're going to be a MP")
        elif number==5:
            print("You're going to be a CM")
        elif number==2:
            print("You're going to be a PM")
        else:
            print("Only numbers 2,3,5,8 are allowed ")
    else:
        print("Only Red, Green, Blue and Yellow are allowed")
print("Enter yes to play again")    
              
        
        
        
