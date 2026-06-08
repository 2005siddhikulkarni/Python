def CountOdd(No):
    Cnt = 0
    digit = 0

    if(No < 0):
        No = - No

    while(No != 0):
        digit = No % 10

        if(digit % 2 != 0):
            Cnt = Cnt + 1

        No = No // 10

    return Cnt

def main():
    print("Enter the value: ")
    Value = int(input())

    result = CountOdd(Value)
    print("Odd numbers are: ",result)

if __name__ == "__main__":
    main()