while True:

    try:
        n = int(input().strip())
        data_in = list(map(int,input().strip().split(" ")))
        res = []
        for i in range(n):
            count = 1
            if i+1<n:
                max_c = data_in[i + 1]
                count += 1
                for j in range(i+2,n):
                    if data_in[j]> max_c:
                        count+=1
                        max_c = data_in[j]
                    else:
                        continue
            if i-1 > -1:
                max_c = data_in[i - 1]
                count += 1
                for j in range(i-2,-1,-1):
                    if data_in[j] > max_c:
                        count += 1
                        max_c = data_in[j]
                    else:
                        continue

            res.append(count)
        res = list(map(str,res))
        print(" ".join(res))
    except:
        break
# print(" ".join(res))
    # except:
    #     break
