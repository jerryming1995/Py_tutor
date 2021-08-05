import collections
import sys
str1= input("输入字符1： ").strip().split(" ")
str2= input("输入字符2： ").strip().split(" ")

if len(str1) != len(str2):
    print(-1)
    sys.exit()

if collections.Counter(str1) != collections.Counter(str2):
    print(-1)
    sys.exit()
res = 0
while(str1 and str2):
    if str1[-1] !=str2[-1]:
        str1.remove(str2[-1])
        res +=1
    else:
        str1.pop()

    str2.pop()
print(res)


