"""Question 2: Fibonacci Sequence
 a program to generate the Fibonacci sequence up to 100."""
num1 = 0
num2 = 1
print(num1)

while num2 < 100:
    print(num2)

    num1, num2 = num2, num1+num2
