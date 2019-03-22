def mynum(x):
    if x > 0:
        if x % 11 == 0:
            return print('%d-11=%d' % (x, x - 11))
        else:
            return print('%d-10=%d' % (x, x - 10))
    elif x < 0:
        if x > -10:
            return print('%d是' % x)
        elif x < -10:
            return print('%d小于-10' % x)
