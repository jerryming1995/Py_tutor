t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    data_in = list(map(int, input().strip().split(" ")))
    res = []
    left = [0]*n
    right = [0]*n


    max_v = data_in[0]

    for i in range(n):

        if data_in[i]>=max_v:
            left[i] = i
            max_v = data_in[i]
        elif data_in[i]<max_v:
            left[i] = left[i-1]

    max_v = data_in[n-1]

    for i in range(n-1,-1,-1):

        if data_in[i] >=max_v:
            right[i] = i
            max_v = data_in[i]
        elif data_in[i]<max_v:
            right[i] = right[i+1]

    print(left)
    print(right)
    for i in range(n):
        count = 0
        if left[i] == i:
            count = count + i
        else:
            count = count + i-left[i]-1
        if right[i] == i:
            count = count + n-1-i
        else:
            count = count + right[i]-i-1
        res.append(count)


    res = list(map(str, res))
    print(" ".join(res))