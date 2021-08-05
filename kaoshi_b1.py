t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    data1 =  list(map(int, input().strip().split(" ")))
    data2 =  list(map(int, input().strip().split(" ")))

    for i in range(n):
        if data1[i]!=data2[i]:
            break
    k = data2[i]-data1[i]
    data1[i] = data1[i] + k
    flag = True
    count = 1
    for j in range(i+1,n):   #只能补一段
        if data1[j] != data2[j]:
            if data2[j]-data1[j]!=k:
                flag = False
                break
            else:
                data1[j] += k
        else:
            break
    for t in range(j,n):
        if data1[t]!=data2[t]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")




