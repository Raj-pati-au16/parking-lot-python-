class RegistrationColour:
    def registration_colour(area, sub_statement):
        if len(sub_statement) == 2:
            colour = sub_statement[1]
            arr = []
            for i in range(len(area)):
                if colour in area[i]:
                    arr.append(area[i][1])
            for j in arr:
                if j == arr[-1]:
                    print(j)
                else:
                    print(j, end=(","))
