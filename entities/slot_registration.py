class SlotRegistration:
    def slot_registration(area, sub_statement):
        if len(sub_statement) == 2:
            for i in range(len(area)):
                if sub_statement[1] in area[i]:
                    print(area[i][0])
                    break
            else:
                print("Not Found")
