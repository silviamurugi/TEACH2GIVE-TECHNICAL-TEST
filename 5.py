'''
Reverse Integer
Write a program that takes an integer as input  and
 returns an integer with reversed digit ordering.
'''

print('Enter Integer to Reverse')
number = input()

reversed = ''
for digit in number:
    reversed = digit + reversed

if '-' in reversed:
    reversed = '-' + reversed[:-1]

reversed = int(reversed)
print(reversed)