from entities.park import Park
from entities.leave import Leave
from entities.status import Status
from entities.registration_colour import RegistrationColour
from entities.slot_colour import SlotColour
from entities.slot_registration import SlotRegistration
from datetime import datetime


class ParkingLot():
    def __init__(self):
        self.area = []
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_day = now.strftime("%d/%m/%Y")

    def create_parkinglot(self, size):
        for i in range(size):
            self.area.append([i + 1])
        print(f"Created a parking lot with {size} slots")

    def activities(self, Statement):
        sub_statement = list(Statement.split())

        if sub_statement[0] == "park" and len(sub_statement) == 3:
            Park.parking(self.area, sub_statement, self.current_day, self.current_time)

        elif sub_statement[0] == "leave":
            Leave.leave(self.area, sub_statement, self.current_day, self.current_time)

        elif sub_statement[0] == "status":
            Status.status(self.area)

        elif sub_statement[0] == "registration_numbers_for_cars_with_colour":
            RegistrationColour.registration_colour(self.area, sub_statement)

        elif sub_statement[0] == "slot_numbers_for_cars_with_colour":
            SlotColour.slot_colour(self.area, sub_statement)

        elif sub_statement[0] == "slot_number_for_registration_number":
            SlotRegistration.slot_registration(self.area, sub_statement)
