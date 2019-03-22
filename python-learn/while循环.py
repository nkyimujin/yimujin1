import random

n = int(random.randint(100, 200))
i = 0
counter = 1
while counter <= n:
    i = i + counter
    counter = counter + 1
print('1到%d相加等于%s' % (n, i))
