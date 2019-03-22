import random
'''
num = int(input('请输入数字'))
if num % 2 == 0:
    if num % 3 == 0:
        print('您输入的数字%s可以被2,3整除' % num)
    else:
        print('您输入的%s只能被2整除' % num)
else:
    if num % 3 == 0:
        print('您输入的数字%s可以被3整除' % num)
    else:
        print('您输入的%s不能被2,3整除' % num)
'''
num = int(random.randint(1,100))
if num%2 == 0:
    if num %3 == 0:
        print('您输入%s可以被2,3整除'%num)
    else:
        print('您输入的%s只能被2整除'%num)
elif num%3==0:
    print('您输入的%s可以被3整除，但不能2被整除'%num)
else:
    print('您输入的数字%s不能被2,3整除'%num)