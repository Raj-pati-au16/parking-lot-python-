class Status:
    def status(area):
        print("Slot No. Registration No Colour")
        for i in area:
            if len(i) == 3:
                for j in i:
                    print(j, end=" ")
                print()
