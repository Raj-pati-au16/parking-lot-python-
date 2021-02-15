class Parking_Lot():
    def __init__(self):
        self.area=[]
    
    def Creat_parking_lot(self,size):
        for i in range(size):
            self.area.append([i+1])
        print(f"Created a parking lot with {size} slots")


    def Activities(self,Statement):
        sub_statement=list(Statement.split())


        if sub_statement[0]=="park":
            if len(sub_statement)==3:
                for i in range (len(self.area)):
                    if len(self.area[i])==1:
                        self.area[i].append(sub_statement[1])
                        self.area[i].append(sub_statement[2])
                        print(f"Allocated slot number: {self.area[i][0]}")
                else:
                    print("Sorry , Parking lot is full")
            else:
                print("You have given a wrong input")


        elif sub_statement[0]=="leave":
            target=(self.area[int(sub_statement[1])-1])
            if len(target)>1:
                while len(target)!=1:
                    target.pop(1)
                print(f"Slot no {sub_statement[1]} is free")
            else:
                print(f"slot no {sub_statement[1]} is already empty")


        elif sub_statement[0]=="status":
            for i in self.area:
                if len(i)==3:
                    for j in i:
                        print(j,end=" ")
                    print()


        elif sub_statement[0]=="registration_numbers_for_cars_with_colour":
            if len(sub_statement)==2:
                colour=sub_statement[1]
                arr=[]
                for i in range (len(self.area)):
                    if colour in self.area[i]:
                        arr.append(self.area[i][1])
                print(arr)
                for j in arr:
                    print(j,end=(","))
                print()


        elif sub_statement[0]=="slot_numbers_for_cars_with_colour":
            if len(sub_statement)==2:
                colour=sub_statement[1]
                arr=[]
                for i in range (len(self.area)):
                    if colour in self.area[i]:
                        arr.append(self.area[i][0])
                for j in arr:
                    print(j,end=(","))
                print()


        elif sub_statement[0]=="slot_number_for_registration_number":
            if len(sub_statement)==2:
                for i in range(len(self.area)):
                    if sub_statement[1] in self.area[i]:
                        print(self.area[i][0])
                        break
                else:
                    print("Not Found")