number = int(input("Enter an integer: "))

sum_digits = 0

while number > 0:
    digit = number % 10
    sum_digits = sum_digits + digit
    number = number // 10

print("Sum of digits is:", sum_digits)
