# Reverse of a number

n = int(input('Enter a number: '))
m = 0
while n != 0:
    a = n % 10
    m = 10 * m + a
    n //= 10

print('Reverse:', m)