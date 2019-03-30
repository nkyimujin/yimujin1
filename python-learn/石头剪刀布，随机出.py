import random
import time

player = int(random.randint(1, 3))  # round(int(input('请输入您要出的拳头：石头=1，剪刀=2，布=3:')))
computer = int(random.randint(1, 3))
# print(time.clock())
print(time.process_time())
if (player < 1 or computer < 1
        or player > 3 or computer > 3):
    print('请输入正确参数')
elif ((player == 1 and computer == 2)
      or (player == 2 and computer == 3)
      or (player == 3 and computer == 1)):
    if player == 1 and computer == 2:
        print('您出的石头，电脑出的布，您获胜')
    elif player == 2 and computer == 3:
        print('您出的剪刀，电脑出的布，您获胜')
    else:
        print('您出的布，电脑出的石头，恭喜获胜')
elif player == computer and player and computer > 0:
    if player == 1:
        a = '都出的石头，平局'
        print(a)
    elif player == 2:
        a = '都出的见到，平局'
        print(a)
    else:
        print('都出的布，平局')
    # print('平局了呢,电脑出的是%s,您出的是%s' % (computer, player))
else:
    if player == 1:
        print('您出的石头，电脑出的布，很遗憾')
    elif player == 2:
        print('您出的剪刀，但是电脑出的布，很遗憾')
    else:
        print('电脑出的布，您出的石头，很可惜')
    # print('连电脑都打不过，渣渣,电脑出的是%s,您出的是%s' % (computer, player))
# print(time.clock())
print(time.process_time())