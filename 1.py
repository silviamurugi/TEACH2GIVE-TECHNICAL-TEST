
'''
Fizbuzz 
Write a program that prints the number from1 to 100.For multiple of 3,print "fizz";
for multiples of 5,print"Buzz";and for numbers that are both 3 and 5,print "FizzBuzz".
'''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')

    elif number % 3 == 0:
        print('Fizz')

    elif number % 5 == 0:
        print('Buzz')