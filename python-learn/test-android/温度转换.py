Tempstr = input('请输入带符号的温度\n')
if Tempstr[-1] in ['F', 'f']:
    C = (eval(Tempstr[:-1]) - 32) / 1.8  # eval 评估函数，去掉最外侧引号并执行余下语句的函数
    print('转换后的温度为{:.2f}C'.format(C))
elif Tempstr[-1] in ['C', 'c']:
    F = (eval(Tempstr[:-1]) * 1.8) + 32
    print('转换后的温度为{:.2f}F'.format(F))
else:
    print('请输入正确的参数\n')
