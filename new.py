"""a=int (input())
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


#for loop
#printing 2 table
for i in range(1,11):
    print(i ,"x 2=",i*2)

i=int(input("Range = "))
n=int(input("Multiplier is : "))
for i in range(1,i+1):
    print(i ,"x" ,n ,"=",i*n)

#printing number between range
a=int(input())
b=int(input())
if(b>a):
    for i in range(a+1,b+1):
        print(i)
else:
    print("enter a valid range")"""

"""
a = int(input())
b = int(input())

if b > a:
    for i in range(a + 1, b + 1):
        if i % 2 == 0:
            print(i)
else:
    print("enter a valid range")

#printing even no.
a=int(input())
b=int(input())
if(b>a):
    for i in range(a+1,b+1):
        if(i%2==0):
            print(i,",")
else:
    print("enter a valid range")

#finding no of terms
a=int(input())
b=int(input())
count=0
if(b>a):
    for i in range(a+1,b+1):
        if(i%2==0):
            count=count+1
    print(count)
else:
    print("enter a valid range")

a=int(input("Number 1:"))
b=int(input("Number 2:"))
ocount=0
ecount=0
for i in range(a,b+1):
    if(i%2!=0):
        ocount=ocount+1
    else:
        ecount=ecount+1
print("Even", ecount)
print("Odd", ocount)

a=int(input("Number 1:"))
b=int(input("Number 2:"))
count=0
for i in range(a,b+1):
    if i%3==0 and i%5==0 :
        count=count+1
print(count)

a=int(input("Numbers :"))
sum=0
for i in range(1,a+1):
    if(i<=a+1):
        sum=sum+i
print("The sum is :",sum)

a=int(input("How many:"))
sum=0
for i in range(1,a+1):
    sum=sum+i
    print(i)
print(sum)

To find cube of a number
a=int(input("How many:"))
cube=0
for i in range(1,a+1):
    cube=i*i*i
    print("The number is",i,"and the cube is",cube)

a=int(input("How many:"))
cube=0
for i in range(1,a+1):
    if(i%7==0 and i%11==0):
        cube=i*i*i
        print("The number is",i,"and the cube is",cube)

a=[]
sum=0
for i in range(9):
    num=int(input())
    a.append(num)
    sum=sum+num
    avg=sum/ len(a)
print(a)
print("The average is", avg)

for i in range(1,5):
    print("week",i)
    for j in range (1,5):
        print("day", j)

for i in range(1):
    print("*")
    for j in range(1):
        print("**")
    for j in range(1):
        print("***")
    for j in range(1):
        print("****")
    for j in range(1):
        print("***")
    for j in range(1):
        print("**")
    for j in range(1):
        print("*")


count=0
for i in range(1,8):
    count=count+i
    if i  !=7 :
        print(i,end="+")
    else:
        print(i,end="")
print("=" ,count)

for i in range(1,4):
    print()
    for j in range(1,i+1):
        if (j==1):
            print("*",end="")
        elif j==2:
            print("**",end="")
        elif j==3:
            print("***",end="")


rows=int(input())
for i in range(1, rows+1):
    print()
    for j in range(1, i + 1):
        print("*", end="")

#while loop

n=int(input())
while (n<11):
    print(n,end="")
    n=n+1


n=int(input())
while(n<=200):
    if(n<200):
        print(n,end=",")
    else:
        print(n,end="")
    n=n+10

n=int(input())
while(n>0):
    if(n<=1):
        print(n,end="")
    else:
        print(n,end=",")
    n=n-1

#to find leap yr or not
year=int(input("Enter the Year = "))
if year%4==0:
    if year%100==0 and year%400==0:
        print("The year has 366 days")
    elif year%100==0 and year%400!=0:
        print("The year has 365 days")
    else:
        print("The year has 366 days")
else:
    print("The year has 365 days")

#to check the number is prime or composite
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Composite")


n=int(input())
factorial=1
for i in range(1,n+1):
    factorial = factorial*i
print(factorial)

#to calc no of digits
n=int(input())
s=str(abs(n))
no_of_digit= len(s)
print(no_of_digit)
 

a=[1,2,3,4,5,6]
print(type(a))
a.insert(5,8)
a.append(7)
a[6]=9
print(a)"""

"""a=[1,2,3,4,5,6]     #list
a.pop(4)
print(a) 
print (a.index(3))
b=[4,5,3,7,8]
a.append(b)
a.extend(b)
print(a)

#tuple
a=(1,2,3,4,5,6)
print(a) 
b=list(a)
print(b)           #elements in tuple can't be modified, but can be casted into list

a={1,2,3,4,5,6,4,5,3,2}   
print(a)
a.remove(5)             #elements are not duplicated, pop removes first element
a.pop()
print(a)

#celsius to Fahreinheit
TEMP =float(input("Enter Temp"))
unit=input("C or K")
Fahreinheit = (TEMP*1.8)+32
if unit=="K" or unit=="k":
    Fahreinheit=(TEMP-273.15)*1.8+32
elif unit=="C" or unit=="c":
    Fahreinheit=(TEMP*1.8)+32
print(Fahreinheit)


name=input("Name")
age=input("Age")
Add=input("Address")
print("Your name is {},your age is {} and you live in {}".format(name,age,Add))""" 

"""while i<=20:
    print(i)
    i=i+1
for i in range (3,21):
    print(i)"""

#Number guessing game

"""import random
randomnum = random.randint(0,50)
Num=int(input("Enter Your Guess between 0 to 50 : "))

if Num>50 or Num<0:
    print("Try numbers between 0 to 50")
elif Num==randomnum:
    print("Muthey! Nee Dhamla")
elif Num>randomnum:
    print("Try out something less")
    Num=int(input("Enter Your Guess between 0 to 50 : "))
elif Num<randomnum: 
    print("Try out something more")
    Num=int(input("Enter Your Guess between 0 to 50 : "))
print(randomnum)"""
   










