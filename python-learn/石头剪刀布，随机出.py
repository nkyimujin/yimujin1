import random

player = int(random.randint(1, 3))  # round(int(input('请输入您要出的拳头：石头=1，剪刀=2，布=3:')))
computer = int(random.randint(1, 3))

if (player < 1 or computer < 1
        or player > 3 or computer > 3):
    print('请输入正确参数')
elif ((player == 1 and computer == 3)
      or (player == 2 and computer == 3)
      or (player == 3 and computer == 1)):
    print('恭喜玩家获胜,电脑出的是%s,您出的是%s' % (computer, player))
elif player == computer and player and computer > 0:
    print('平局了呢,电脑出的是%s,您出的是%s' % (computer, player))
else:
    print('连电脑都打不过，渣渣,电脑出的是%s,您出的是%s' % (computer, player))
