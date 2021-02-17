from entities.park import park
from entities.leave import leave
from entities.status import status
from entities.registration_colour import registrationColour
from entities.slot_colour import slotColour
from entities.slot_registration import slotRegistration

class parkingLot():
    def __init__(self):
        self.area=[]
        self.park=park()
        self.leave=leave()
        self.status=status()
        self.registrationColour=registrationColour()
        self.slotColour=slotColour()
        self.slotRegistration=slotRegistration()

    def create_parkinglot(self,size):
        for i in range(size):
            self.area.append([i+1])
        print(f"Created a parking lot with {size} slots")


    def activities(self,Statement):
        sub_statement=list(Statement.split())


        if sub_statement[0]=="park" and len(sub_statement)==3:
            park.parking(self.area,sub_statement)
            

        elif sub_statement[0]=="leave":
            leave.leave(self.area,sub_statement)


        elif sub_statement[0]=="status":
            status.status(self.area)


        elif sub_statement[0]=="registration_numbers_for_cars_with_colour":
            registrationColour.registration_colour(self.area,sub_statement)


        elif sub_statement[0]=="slot_numbers_for_cars_with_colour":
            slotColour.slot_colour(self.area,sub_statement)

        elif sub_statement[0]=="slot_number_for_registration_number":
            slotRegistration.slot_registration(self.area,sub_statement)