def mynum(x):
    if x > 0:
        if x % 11 == 0:
            b = x + 10
            a = '%d+10=%d' % (x, b)
            return a
        else:
            b = x + 10
            a = '%d+10=%d' % (x, b)
            return a
    elif x < 0:
        if x > -10:
            b = x + 10
            a = '%d+10=%d' % (x, b)
            return a
        elif x < -10:
            b = x + 10
            a = '%d+10=%d' % (x, b)
            return a
