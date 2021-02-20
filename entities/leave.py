class Leave:
    def leave(area, sub_statement, current_day, current_time):
        target = (area[int(sub_statement[1]) - 1])
        if len(target) > 1:
            print(f"Slot no {sub_statement[1]} is free and was occupied from {area[int(sub_statement[1]) - 1][3]},{area[int(sub_statement[1]) - 1][4]} to {current_day},{current_time}")
            while len(target) != 1:
                target.pop(1)

        else:
            print(f"slot no {sub_statement[1]} is already empty")
