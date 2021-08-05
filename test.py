
while True:
    try:
        line1 = input().strip().split(" ")
        N = int(line1[0])
        M = int(line1[1])
        student = input().strip().split(" ")
        student = list(map(int, student))


        def q_operation(opera):

            start = min(int(opera[0]), int(opera[1])) - 1
            end = max(int(opera[0]), int(opera[1]))       #这是一个难点
            # queue = sorted(opera)
            # start = int(queue[0]) - 1
            # end = int(queue[1])
            return max(student[start:end])


        def u_operation(opera):
            index = int(opera[0]) - 1
            grade = int(opera[1])
            student[index] = grade

        for i in range(M):
            temp = input().strip().split(" ")
            if temp[0] == "Q":
                print(q_operation(temp[1:]))
            if temp[0] == "U":
                u_operation(temp[1:])
    except:
        break






