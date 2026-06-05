
def ChkZero(Value):
    digit = 0

    if(Value < 0):
        Value = -Value

    while(Value != 0):
         digit = Value % 10

         if(digit == 0):
            return True

         Value = Value // 10

    return False

def main():
    print("Enter the number: ")
    No = int(input())

    ans = ChkZero(No)

    if(ans == True):
        print("It contains zero")

    else:
        print("It does not contains zero")

if __name__ == "__main__":
    main()

