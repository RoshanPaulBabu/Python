def calculate(a,r,m):
    ri = r/100/12
    p = ri*a/(1-(1+ri)**-m)
    return p
    
print("LOAN AMOUNT CALCULATOR")
print("="*25)

a = int(input("Enter the loan amount: "))
r = int(input("Enter the annual interest rate(%): "))
m = int(input("Enter the number of months: "))

p = calculate(a,r,m)

print("\nLoan Details: ")
print(f"Loan Amount: ${r}%")
print(f"Number of months: {m}")
print(f"Monthly Payment Amount: ${p:.2f}")


