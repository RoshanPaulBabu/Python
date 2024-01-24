import random

    
def main():
    num = int(input("Enter the number of questions: "))
    for i in range(1,num+1):
        print("Question ",i)
        n1 = random.randint(1,10)
        n2 = random.randint(1,10)
        print(n1,"+",n2,"=","_____")
        print()
    main()


print("Printable Addition Test")
print("="*23)
main()

