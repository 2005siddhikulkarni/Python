def DisplayDigit(string):
   
    for ch in string:
        if(ch >= "0" and ch <= "9"):
            print(ch,end = "")
    
def main():
    print("Enter the string: ")
    string = input()

    DisplayDigit(string)

if __name__ == "__main__":
    main()