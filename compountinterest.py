PA = input("Enter the principal amount: ")
T = input("Enter the time: ")
R = input("Enter the rate: ")

CompoundInterest = float(PA) * (1 + float(R) / 100) * float(T)
print(CompoundInterest)
