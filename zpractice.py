##print("Prime numbers up to 100: ")
##
##for i in range(2,101):
##    for j in range(2,i):
##        if i%j == 0:
##            break
##
##    else:
##        print(i, end= " ")
##
##_________________________________________________________
##
##print("Armstrong numbers from 1 to 1000:")
##
##for i in range(1,1000):
##    sum = 0
##    string = str(i)
##    dig = len(string)
##
##    for j in string:
##        sum += int(j)**dig
##    if sum == i:
##        print(i,end=" ")
##__________________________________________________________
##
##
##num = int(input("Enter the number of terms in the Fibinacci Series: "))
##
##
##x= 0
##y=1
##for i in range(num):
##    print(x, end = " ")
##    z= x+y
##    x = y
##    y = z
##    
##___________________________________________________________
##
##num = int(input("Enter a number to check the factorial: "))
##temp = num
##sum = 1
##for i in range(num):
##    sum *=  num
##    num -= 1
##
##print(f"Factorial of {temp} is: {sum}")
##_____________________________________________________________
##
##import random
##
##print("I've selected a random two-digit number between 10 and 99")
##
##print("Can you guess what it is?")
##
##com = random.randint(10,99)
##while True:
##    num = int(input("Enter your guess: "))
##
##    if com == num:
##        print(f"Congratulations! You guessed it: {com}")
##        break
##    elif num>com:
##        print("Too High.")
##    else:
##        print("To Low.")
##
##______________________________________________________________
##
##
##for i in range(1,20):
##    if i%3 == 0 and i%5 == 0:
##        print("FizzBuzz",end=" ")
##    elif i%3 == 0:
##        print("Fizz",end=" ")
##    elif i%5 == 0:
##        print("Buzz",end =" ")
##    else:
##        print(i,end= " ")
##_______________________________________________________________
##
##a = int(input("Enter a: "))
##b = int(input("Enter b: "))
##c = int(input("Enter c: "))
##d = b**2-(4*a*c)
##
##root1 = (-b + d**0.5)/2*a
##root2 = (-b - d**0.5)/2*a
##
##print(f"Real roots: Root 1 = {root1} Root 2 = {root2}")
##
##________________________________________________________________
##
prin = int(input("Enter the principal amount:- "))
rate = float(input("Enter the rate of interest:- "))
time = int(input("Enter the time period"))

for i in range(time):
    sum += (prin*rate)
print(sum)
##________________________________________________________________
##
##print("Multiplication Table: ")
##print("   ", end= " ")
##for i in range(1,11):
##    print(f"{i:5}", end= "")
##print("\n","-"*53)
##for j in range(1,11):
##    print(f"{j:2}","|",end=" ")
##    for k in range(1,11):
##        print(f"{(j*k):4}",end=" ")
##    print()
##_________________________________________________________________
##
##
##num = int(input("Enter a number: "))
##for i in range(num+1):
##    print(" "*(num-i),"*"*((2*i)-1))
