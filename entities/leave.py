class leave:
    def leave(area, sub_statement):
        target = (area[int(sub_statement[1])-1])
        if len(target) > 1:
            while len(target) != 1:
                target.pop(1)
            print(f"Slot no {sub_statement[1]} is free")
        else:
            print(f"slot no {sub_statement[1]} is already empty")
