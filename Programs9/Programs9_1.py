
def DisplayDigit(Value):
    digit = 0

    if(Value < 0):
        Value = -Value

    else:

        while(Value != 0):
            digit = Value % 10
           
            print(digit)
            Value = Value // 10
        

def main():
    print("Enter the number: ")
    No = int(input())

    DisplayDigit(No)

if __name__ == "__main__":
    main()