def DisplayConvert(ch):

    if(ch >= "a" and ch <= "z"):
        New_ch = ch.upper()
        print("The converted character is: ",New_ch)

    elif(ch >= "A" and ch <= "Z"):
        New_ch = ch.lower()
        print("The converted character is: ",New_ch)

def main():

    print("Enter the character: ")
    ch = input()

    DisplayConvert(ch)

if __name__ == "__main__":
    main()