def DisplaySchedule(ch):

    if(ch == "A" or ch == "a"):
        print("your exam at 7.00 AM")

    elif(ch == "B" or ch == "b"):
        print("your exam at 8.30 AM")

    elif(ch == "C" or ch == "c"):
        print("your exam at 9.20 AM")

    elif(ch == "D" or ch == "d"):
        print("your exam at 10.30 AM")

def main():
    print("Enter the character: ")
    ch = input()

    DisplaySchedule(ch)

if __name__ == "__main__":
    main()