class park:
    def parking(area, sub_statement):
        temp = "false"
        for i in range(len(area)):
            if len(area[i]) == 1:
                area[i].append(sub_statement[1])
                area[i].append(sub_statement[2])
                print(f"Allocated slot number: {area[i][0]}")
                temp = "true"
                break
        if temp == "false":
            print("Sorry , Parking lot is full")
