line1 = input().strip().split(" ")
m = int(line1[0])
n = int(line1[1])
line2 = input().strip().split(" ")
d1 = list(map(int,line2))
line3 = input().strip().split(" ")
d2 = list(map(int,line3))

d1 = sorted(d1)[::-1]
d2 = sorted(d2)[::-1]
def discount(goods):
    for i in range(m):
        if d1[i]<=goods:
            return goods-d1[i]
    return goods              #无折可打
res = 0
for i in range(n):
    res = res + discount(d2[i])
print(res)

