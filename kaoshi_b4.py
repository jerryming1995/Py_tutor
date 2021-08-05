t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    data_in = list(map(int, input().strip().split(" ")))
    res = []
    for i in range(n):
        count = 0
        for j in range(i,-1,-1):
            if data_in[j]<=data_in[i]:
                count +=1
            else:
                break
        for j in range(i+1,n):
            if data_in[j]<=data_in[i]:
                count +=1
            else:
                break
        res.append(count-1)
    res = list(map(str, res))
    print(" ".join(res))