
def isprime(num):
    for j in range(2,num):
        if num % j == 0:
            return False
            break
    else:
        return True

    
num = int(input("Enter a number: "))

if isprime(num):
    print(f"Your number {num} is prime")

else:
    print(f"Your number {num} is  not prime")
