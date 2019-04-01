num_to_math = "零一二三四五六七八九"
s = input()
for c in s:
    print(num_to_math[eval(c)], end="")
