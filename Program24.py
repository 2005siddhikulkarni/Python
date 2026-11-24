class Arithmatic:

    def Addition(self, iNo1, iNo2):
        iAns = 0

        iAns = iNo1 + iNo2

        return iAns

def main():
    iValue1 = 0
    iValue2 = 0
    iResult = 0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    arithmatic = Arithmatic()

    iResult = arithmatic.Addition(iValue1, iValue2)
    print("Addition is: ",iResult)

if __name__ == "__main__":
    main()