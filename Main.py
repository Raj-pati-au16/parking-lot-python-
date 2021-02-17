from interactive import interactive
from file_input import fileInput



if __name__ == "__main__":

    print("There are 2 type of interaction available. 1.interactive for manual input. 2.file input for giving input in a file")
    interaction=input("write interactive or file to choose from them :")
    print()
    manual=interactive()
    auto=fileInput()

    if interaction=="interactive":
        cnt=0
        while cnt<2:
            if cnt==0:
                manual.create_Parking()
                cnt+=1
            else:
                manual.activities()
                cnt+=1
        
    
    elif interaction=="file":
        file_address="C:\\Users\Raj\Desktop/new.txt"
        f= open(file_address,"r")
        cnt=0
        for row in f:
            if cnt==0:
                auto.create_Parking(row)
                cnt+=1
            else:
                auto.activities(row)

