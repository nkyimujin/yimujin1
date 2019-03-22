a = [2, 2, 4, 5, 6, 7, 8, 9, 3]
L = [7, 8]
print(a.count(1), a.count(2), a.count(5))  # list.count(x)返回x在列表中出现的次数
a.append(12)  # list.append在列表尾部添加一个元素相当于a[len(a):]=[s]
print(a)
a.remove(2)  # list.remove(X)删除列表值为x的第一个元素，如果没有会报错
print(a)
a.extend(L)  # list.exend(L)通过指定列表，拓展所有元素到列表
print(a)
a.insert(5, 5)  # list.insert(2,x)在指定2的位置添加元素x
print(a)
# a.pop(6)#list.pop([2])从列表指定2位置移除元素并输出，没有创建索引，a.pop()返回最后一个，花括号可选
print(a.pop(6))
print(a)
a.sort()  # list.sort()对list列表元素进行排序
print(a)
L.reverse(), a.reverse()  # list.reverse()对list列表中的元素进行倒排
print(a, L)
print(a.copy())  # 返回到列表的浅复制，相当于a[:]
a.clear()  # list.clear移除表中所有元素，相当于del a[:]
print(a)
