def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    else:
        return True



n = int(input("Please enter a number to check if it is prime or not: "))
if is_prime(n) == True:
            print("Your number",n,"is a prime number")

elif is_prime(n) == False:
                print("Your number",n,"is not a prime number")

  
    
