
a=[]
result=input().split(' ')
N=int(result[0])
L=int(result[1])

i = L
while i <= 100:
    a = (2 * N - i*(i - 1)) / (2 * i)
    if int(a) == a:
        for j in range(i- 1):
            print(int(a), end=" ")
            a += 1
        print(int(a))
        break
    i += 1
if i == 101:
    print("No")