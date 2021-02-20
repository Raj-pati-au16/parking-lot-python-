class Park:
    def parking(area, sub_statement, current_day, current_time):
        temp = "false"
        for i in range(len(area)):
            if len(area[i]) == 1:
                area[i].append(sub_statement[1])
                area[i].append(sub_statement[2])
                area[i].append(current_day)
                area[i].append(current_time)
                print(f"Allocated slot number: {area[i][0]} on {current_day} , at {current_time}")
                temp = "true"
                break
        if temp == "false":
            print("Sorry , Parking lot is full")
