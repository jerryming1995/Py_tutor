n = int(input().strip())
line1 = input().strip().split(" ")
d1 = list(map(int,line1))

count=[0]

def cut(current,m,n):
    if m<=current<=n:
        return
    # print(current)

    left = current//2
    right = current-left
    if left>=right:
        left,right = right,left
    count[0] +=1
    cut(left,m,right)
    cut(right,left,n)

res = 0
for i in range(1,n-1):
    count[0] = 0
    if d1[i]>=d1[i-1] and d1[i]<=d1[i+1]:
        continue
    else:
        cut(d1[i],d1[i-1],d1[i+1])
        d1[i] = d1[i-1]+1
        res = res+count[0]

print(res)

