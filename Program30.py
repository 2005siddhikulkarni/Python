def Average(iNo1, iNo2):
    fAns = 0.0

    fAns = (iNo1 + iNo2) / 2

    return fAns

def main():
    iValue1 = 0
    iValue2 = 0
    fResult = 0.0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    fResult = Average(iValue1, iValue2)
    print("Average is: ",fResult)

if __name__ == "__main__":
    main()