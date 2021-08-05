import sys
N = int(sys.stdin.readline().strip())
line_1 = sys.stdin.readline().strip().split(' ')
n= int(line_1[0])
m = int(line_1[1])
res = []
for i in range(1,n):
        # 读取每一行\
    temp = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
    res.append(temp.split(""))