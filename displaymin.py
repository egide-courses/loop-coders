
number = int(input("Enter numberber 1: "))
maximum = number
minimum = number

for i in range(2, 11):
    numberber = int(input("Enter numberber " + str(i) + ": "))

    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

print("Maximum number is:", maximum)
print("Minimum numberr is:", minimum)
