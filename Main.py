from Creating_parking_lot import Parking_Lot
if __name__ == "__main__":
    print("There are 2 type of interaction available. 1.interactive for manual input. 2.file input for giving input in a file")
    interaction=input("write interactive or file to choose from them :")
    obj=Parking_Lot()

    if interaction=="interactive":
        cnt=0
        exit="False"
        while exit=="False":
            obj.Creat_parking_lot()
        
    
    elif interaction=="file":
        f= open("C:\\Users\Raj\Desktop/new.txt","r")
        cnt=0
        for x in f:
            if cnt==0:
                print(x)
                cnt+=1
