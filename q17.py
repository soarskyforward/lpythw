s = input("Input your string ")

letters = 0
space = 0
digits = 0
others = 0

for i in s:
    if i.isalpha():
        letters += 1
    if i.isspace():
        space += 1
    if i.isdigit():
        digits += 1
    else:
        others += 1

print("char=", letters)


# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
