while(1):
    try:
        pokes = input().strip().split("-")
        player1 = pokes[0]
        player2 = pokes[1]

        max_p = "joker JOKER"

        table = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A","joker","JOKER"]

        print(player1)
        print(player2)
        if player1 ==max_p:
            print(player1)
            continue
        if player2 ==max_p:
            print(player2)
            continue

        p1 = player1.split(" ")
        p2 = player2.split(" ")
        if len(p1) == 4 and len(p2)!=4:
            print(player1)
            continue

        if len(p2) == 4 and len(p1)!=4:
            print(player1)
            continue

        if len(p1)!=len(p2):
            print("ERROR")
            continue

        if len(p1)==len(p2):
            if table.index(p1[0])>table.index(p2[0]):
                print(player1)

            else:
                print(player2)
    except:
        break



