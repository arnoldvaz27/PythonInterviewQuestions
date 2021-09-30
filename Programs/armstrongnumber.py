def armstrongNumber(arm):
    number = 0
    for x in arm:
        number = number + (int(x) ** 3)

    print("The given number is armstrong" if number == int(arm) else "The given number is not armstrong")


arms = input("Enter a number: ")
armstrongNumber(arms)
