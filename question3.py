"""Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two."""

n = int(input("Enter a number: "))
if n <= 0:
    print("number should be greator than 0")
else:
    is_power_of_two = False
    for i in range(n):
        if 2 ** i == n:
            is_power_of_two = True
            break
        elif 2 ** i > n:
            break
    print(is_power_of_two)

