def MultDigit(No):
    Cnt = 1
    digit = 0
    

    while(No != 0):
        digit = No % 10

        Cnt = Cnt * digit

        No = No // 10

    return Cnt

def main():
    print("Enter the value: ")
    Value = int(input())

    result = MultDigit(Value)
    print("Multiplication is: ",result)

if __name__ == "__main__":
    main()