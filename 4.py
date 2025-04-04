'''
Capilatize Every Word
Write a program that accepts a string as input,capitalizes the first letter of each word in the string,
and then returns the result string.
'''

print('Type the Word to Capitalize')
string = input()

#break the string into array of individual words
words = string.split(' ')

output = ''
for word in words:
    output = output + word.capitalize() + ' '

print(output)