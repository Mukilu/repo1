a=int (input())
b=int (input())
c=a+b
print(c)

a=input()
b=input()
print("My name is ",a)
print("My age is ",b)

a=int (input())
b=int (input())
c=int (input())
d=(a*b*c)
e=(a+b+c)
f=int(d/e)
print("The Result is" ,f)

name=input()
score= int (input())
dep=input()
a=score/10
print(name)
print("My SCORE IS :",a,"/10")
print(dep)

Meghna=input()
if (Meghna=="Died"):
    print("Suriya meets Priya")
else:
    print("Suriya weds Meghna")

mark=int (input())
if (mark>35):
    print("Pass")
else:
    print("Fail")

Amount=int(input("Enter your Annual income"))
if(Amount>70000):
    print("Not eligible for Scholarship")
else:
    print("Eligible for Scholarship")

user=int(input("Enter a number : "))
if(user%15==0):
    print("Number is divisible by 3 and 5")
else:
    print("Not valid")

user=int(input("Enter a number"))
if(user%2==0):
    print("Number is even")
else:
    print("Odd")

user=int(input("Value : "))
if(user%8==0 and user%5!=0):
     print("Valid")
else:
     print("Not valid")

user=int(input("Score : "))
if(user<35):
     print("C")
elif(user>=35 and user<=70):
     print("B")
elif(user>70 and user<=100):
     print("A")
else:
     print("Invalid Input")

a=int(input("n1 :"))
b=input("Operator :")
c=int(input("n2 :"))
if(b=="+"):
    print(a+c)
elif(b=="-"):
    print(a-c)
elif(b=="*"):
    print(a*c)
elif(b=="/"):
    print(a/c)
else:
    print("Syntax Error")

Score=int(input("Input Score"))
if(Score>70):
    name=input()
    department=input()
    print("Eligible")
else:
    print("Not Eligible") 

salary=int(input("Input ur salary"))
age=int(input("Age"))
if(salary>=20000 or age<=25):
   amountrequired=int(input("Loan amount required"))
   if(amountrequired<=50000):
      print("Eligible")
   if(amountrequired<=0):
      print("Invalid amount") 
   else:
      print("Maximum amount is 50000")
else:
   print("Not Eligible")

a=int(input("s1"))
b=int(input("s2"))
c=int(input("s3"))
d=int(input("s4"))
e=int(input("s4"))
avg=(a+b+c+d+e)/5
print(avg)
if(avg<35):
    print("Need more classes")
else:
    print("Good to go")

a=int(input())
if(a%2==0):
    if(a>=2 and a<=5):
        print("Big Weird")
    elif(a>=6 and a<=20):
        print("Bigger Weird")
    elif(a>20):
        print("Biggest Weird")
else:
    print("Weird")










