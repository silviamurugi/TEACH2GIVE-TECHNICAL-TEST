'''
count vowels
Write a program that counts the number of vowels in a sentence.
'''

vowels = ['a', 'e', 'i', 'o', 'u']

print('Enter String to count vowels:')
sentense = input()
sentense = sentense.lower()
counter = 0

for vowel in vowels:
    if vowel in sentense:
        counter = counter + 1

print(counter)