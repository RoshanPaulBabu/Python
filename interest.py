prin = int(input("Enter the principal amount:- "))
rate = float(input("Enter the rate of interest:- "))
time = int(input("Enter the time period"))
sum = prin
i =0
while time != i:
    sum =sum + (sum * rate)
    i += 1
print(sum)

