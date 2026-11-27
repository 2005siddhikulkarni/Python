def Maximum(iNo1, iNo2, iNo3):
    if((iNo1 > iNo2) and (iNo1 > iNo3)):
        return iNo1

    elif((iNo2 > iNo1) and (iNo2 > iNo3)):
        return iNo2

    else:
        return iNo3

def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    iResult = 0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    print("Enter the third number: ")
    iValue3 = int(input())

    iResult = Maximum(iValue1, iValue2, iValue3)
    print("Maximum is: ",iResult)

if __name__ == "__main__":
    main()