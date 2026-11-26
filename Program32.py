class A:
    def Average(self, iNo1, iNo2, iNo3):
        fAns = 0.0

        fAns = (iNo1 + iNo2 + iNo3) / 3

        return fAns

def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    fResult = 0.0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    print("Enter the third number: ")
    iValue3 = int(input())

    a = A()

    fResult = a.Average(iValue1, iValue2, iValue3)
    print("Average is: ",fResult)

if __name__ == "__main__":
    main()