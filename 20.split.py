str1 = "one two three four"
str2 = "10:20:30:40:50"
str3 = "a/b/c/d/e/f"

x= str1.split()
y = str2.split(":")
z = str3.split("/")

for i in x:
    print(f"Token: {i}")

print()

for i in y:
    print(f"Token: {i}")

print()

for i in z:
    print(f"Token: {i}")
