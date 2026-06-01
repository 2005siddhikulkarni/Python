def DollarToInt(Value):
    DollarPrice = 70

    if(DollarPrice == 70):
        return DollarPrice * Value

def main():
    print("Enter the number: ")
    Value = int(input())

    ans = DollarToInt(Value)
    print("Value of INR is: ",ans)

if __name__ == "__main__":
    main()