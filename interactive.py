from Creating_parking_lot import Parking_Lot

class Interactive:
    def __init__(self):
        self.obj=Parking_Lot()
    def Create_Parking(self):
        User_Input=list(input("Creat a parking lot :").split())
        size=int(User_Input[1])
        self.obj.Creat_parking_lot(size)

    def Activities(self):
        User_Input=input()
        while User_Input !="exit":
            self.obj.Activities(User_Input)
        print("exit")