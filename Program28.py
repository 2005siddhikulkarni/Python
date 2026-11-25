def Maximum(iNo1, iNo2):

    if(iNo1 > iNo2):
       return iNo1
    
    else:
       return iNo2

def main():
    iValue1 = 0
    iValue2 = 0
    iResult = 0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    iResult = Maximum(iValue1, iValue2)
    print("Maximum is: ",iResult)

if __name__ == "__main__":
    main()