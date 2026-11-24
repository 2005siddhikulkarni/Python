def Maximum(iNo1, iNo2):

    if(iNo1 > iNo2):
        print("Maximum is: ",iNo1)
    
    else:
        print("Maximum is: ",iNo2)

def main():
    iValue1 = 0
    iValue2 = 0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    Maximum(iValue1, iValue2)

if __name__ == "__main__":
    main()