"""
Question -

Python program to add 2 numbers

"""

# Code -
# 1st method
num1, num2 = 3, 5
print(num1 + num2)

# 2nd method
firstInput = input("Enter the first number: ")
secondInput = input("Enter the second number: ")
print(int(firstInput) + int(secondInput))

# 3rd method
i = 1
k = list()
while i <= 2:
    Input = input("Enter the number: ")
    k.append(int(Input))
    i = i + 1

print(sum(k))

# 4th method
print("Sum of {0} and {1} is {2}".format(num1, num2, (num1 + num2)))

"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
