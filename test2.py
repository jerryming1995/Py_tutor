import sys
import collections
dic = collections.OrderedDict()   #注意：因为要根据输入时间排序，所以必须是OrderedDict()!!!!!
while True:
    try:
        data_in = input().strip().split("\\")
        key = data_in[-1]
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    except:
        break

output = sorted(dic.items(),key=lambda x: x[1],reverse= True)
cnt = 0
for value in output:

    if cnt<8:
        temp0 = value[0].split(" ")[0]

        temp1 = value[0].split(" ")[1]
        if len(temp0)>16:
            print(temp0[-16:]+" "+temp1+" "+str(value[1]))
        else:
            print(temp0+" "+temp1+" "+str(value[1]))
        cnt +=1
    else:
        break



