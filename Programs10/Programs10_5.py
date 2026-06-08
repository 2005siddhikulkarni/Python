def CntEvenOdd(No):
    Even = 0
    Odd = 0
    digit = 0

    if(No < 0):
        No = -No
    
    while(No != 0):
        digit = No % 10
        No = No // 10

        if(digit % 2 == 0):
            Even += digit

        else:
            Odd += digit

    diff = Even - Odd

    return diff

def main():
    print("Enter the value: ")
    Value = int(input())

    result = CntEvenOdd(Value)
    print("The difference between even and odd is: ",result)

if __name__ == "__main__":
    main()