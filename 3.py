'''
Power of 2
Write a program that takes an integer as input and returns true if the input is a power of two.
'''

print('Type the Number to Check:')
number = int(input())

while number > 1 and number % 2 == 0:
    number = number / 2

print(True if number == 1 else False)
