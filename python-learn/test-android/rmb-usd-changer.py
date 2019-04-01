# u = input()
# if u[0] in ['F','f']:
#     C = (eval(u[1:])-32)/1.8
#     print('C{:.2f}'.format(C))
# elif u[0] in ['C','c']:
#     F = eval(u[1:])*1.8 +32
#     print('F{:.2f}'.format(F))
u = input()
if u[:3] in ['RMB', 'rmb']:
    USD = eval(u[3:]) / 6.78
    print('USD{:.2f}'.format(USD))
elif u[:3] in ['USD', 'usd']:
    RMB = eval(u[3:]) * 6.78
    print('RMB{:.2f}'.format(RMB))
