'''
Fibonacci Sequence 
Write a program to genarete the fibonacci sequence up to 100.
'''

a = 0
b = 1
fibanocci = [a, b]

while True:
    c = a + b 
    if c <= 100:
        fibanocci.append(c)
        a = b
        b = c
    else:
        break

print(fibanocci)