from managingparkinglot import parkingLot


class fileInput:
    def __init__(self):
        self.obj = parkingLot()

    def create_Parking(self, row):
        user_input = list(row.split())
        size = int(user_input[1])
        self.obj.create_parkinglot(size)

    def activities(self, row):
        user_Input = row
        self.obj.activities(user_Input)
