"""Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2"""


string = "hello world"
vowels = ("a", "e", "i", "o", "u")
count = 0

for vowel in vowels:
    if string.lower().count(vowel) >= 1:
        count += 1

print(count)
