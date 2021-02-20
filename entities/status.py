class Status:
    def status(area):
        print("Slot No. Registration No Colour")
        for i in area:
            if len(i) == 5:
                cnt = 0
                for j in i:
                    if cnt < 3:
                        print(j, end=" ")
                        cnt += 1
                print()
