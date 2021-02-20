from managingparkinglot import ParkingLot


class Interactive:
    def __init__(self):
        self.obj = ParkingLot()

    def create_Parking(self):
        User_Input = list(input("Creat a parking lot :").split())
        size = int(User_Input[1])
        self.obj.create_parkinglot(size)

    def activities(self):
        temp = "true"
        while temp == "true":
            User_Input = input()
            if User_Input == "exit":
                temp = "false"
                break
            else:
                self.obj.activities(User_Input)
