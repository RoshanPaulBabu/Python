a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

deter = (b * b) - 4 * a * c

root1 = (-b + deter ** 0.5)/2*a
print("root1: ", root1)

root2 = (-b - deter ** 0.5)/2*a
print("root2: ", root2)
