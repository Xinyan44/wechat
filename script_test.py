f = open('./魔道祖师.txt',encoding='gbk', errors='ignore')
txt = []
for line in f:
    txt.append(line.strip())

find = False
for line in range(len(txt)):
    if '抱' in txt[line]:
        print(txt[line - 5])
        print(txt[line - 4])
        print(txt[line - 3])
        print(txt[line - 2])
        print(txt[line - 1])
        print(txt[line])
        print(txt[line + 1])
        print(txt[line + 2])
        print(txt[line + 3])
        print(txt[line + 4])
        print(txt[line + 5])
        find = True
        break

if not find:
    print('这个字小说里面没有~')

