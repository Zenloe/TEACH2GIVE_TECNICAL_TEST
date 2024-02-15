"""Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19"""


def reverse_digits(num):
    reverse = int(str(abs(num))[::-1])
    return reverse if num >= 0 else -reverse

print(reverse_digits(500))
print(reverse_digits(-56))
print(reverse_digits(-90))
print(reverse_digits(91))

