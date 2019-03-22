a = [1, 3, 4, 5, 7]
print(a)
print(a.append((int(input('请输入要添加到列表的数字\n')))))
if True:
    print(a)
a.append(1)
print(a)
a.sort()
x = len(a)  # len(list)统计列表中的元素数量
while x > 0:
    x = x - 1
    print(a.pop())
print('此程序为添加一个元素到列表尾部，并从尾部删除元素')
