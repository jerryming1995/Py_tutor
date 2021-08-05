

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         print(values)
#         for v in values:
#             # print(v)
#             ans += v2


# import sys
# print("输入行与列：")
# result = sys.stdin.readline().strip().split(" ")
# m = int(result[0])
# n= int(result[1])
# board = []
# for i in range(m):
#     print("输入第{}行: ".format(i))
#     line = sys.stdin.readline().strip().split(" ")
#     if len(line) != n:
#         print("输入错误")
#         sys.exit()
#     print(line)
#     board.append(line)
#
# print(board)

import sys
result= input("输入行与列: ").strip().split(" ")
result = list(map(int,result))
m= result[0]
n= result[1]
board=[]
for i in range(m):
    temp=input("输入第{}行: ".format(i)).strip().split(" ")
    if len(temp)!=n:
        print("输入错误")
        sys.exit()
    board.append(temp)

print(board)
