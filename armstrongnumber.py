Input = input("Enter a number: ")
number = 0
for x in Input:
    number = number + (int(x) ** 3)

print("The given number is armstrong" if number == int(Input) else "The given number is not armstrong")
