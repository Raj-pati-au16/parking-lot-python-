from interactive import Interactive
from file_input import File



if __name__ == "__main__":

    print("There are 2 type of interaction available. 1.interactive for manual input. 2.file input for giving input in a file")
    interaction=input("write interactive or file to choose from them :")
    manual=Interactive()
    auto=File()

    if interaction=="interactive":
        cnt=0
        while cnt<2:
            if cnt==0:
                manual.Create_Parking()
                cnt+=1
            else:
                manual.Activities()
        
    
    elif interaction=="file":
        f= open("C:\\Users\Raj\Desktop/new.txt","r")
        cnt=0
        for row in f:
            if cnt==0:
                auto.Create_Parking(row)
                cnt+=1
            else:
                auto.Activities(row)
