from interactive import Interactive
from file_input import FileInput
if __name__ == "__main__":

    print("Type interactive for manual input or file for auto inputs.")
    interaction = input("write interactive or file to choose from them :")
    print()
    manual = Interactive()
    auto = FileInput()

    if interaction == "interactive":
        cnt = 0
        while cnt < 2:
            if cnt == 0:
                manual.create_Parking()
                cnt += 1
            else:
                manual.activities()
                cnt += 1

    elif interaction == "file":
        file_address = "new.txt"
        f = open(file_address, "r")
        cnt = 0
        for row in f:
            if cnt == 0:
                auto.create_Parking(row)
                cnt += 1
            else:
                auto.activities(row)
