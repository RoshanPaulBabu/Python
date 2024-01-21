a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - (4*a*c)

root1 = (-b + (d ** 0.5))/2*a
root2 = (-b - (d ** 0.5))/2*a

print(f"Real roots: Root 1 = {root1} Root 2 = {root2}")
