def CountRange(No):
    Cnt = 0
    digit = 0

    while(No != 0):
        digit = No % 10

        if(digit > 3 and digit < 7):
            Cnt += 1

        No = No // 10

    return Cnt

def main():
    print("Enter the value: ")
    Value = int(input())

    result = CountRange(Value)
    print("numbers are: ",result)

if __name__ == "__main__":
    main()