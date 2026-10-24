def Addition(iNo1, iNo2):
    iAns = 0

    iAns = iNo1 + iNo2

    print("Addition is: ",iAns)

def main():
    iValue1 = 0
    iValue2 = 0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    Addition(iValue1, iValue2)

if __name__ == "__main__":
    main()