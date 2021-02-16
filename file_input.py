from Managing_parking_lot import Parking_Lot

class File:
    def __init__(self):
        self.obj=Parking_Lot()


    def Create_Parking(self,row):
        user_input=list(row.split())
        size=int(user_input[1])
        self.obj.Create_parking_lot(size)

    def Activities(self,row):
        User_Input=row
        cnt=0
        self.obj.Activities(User_Input)
            