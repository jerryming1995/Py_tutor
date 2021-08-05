
result=input()

n = int(result[0])

devided = 1e9 + 7

def combine(n,i):
    fenmu = 1
    fenzi = 1
    for j in range(n,n-i,-1):
        fenzi = fenzi * j
    for j in range(1,i+1):
        fenmu = fenmu*j

    return int(fenzi/fenmu)
if n<=1:
    res = 1
    print(int(res % devided))
else:
    res = 0
    for i in range(1,n+1):
        res = res + i*combine(n,i)

    print(int(res%devided))
dp = [0]*(n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1]*2 + dp[i-1] * i

print(dp[-1]%devided)

