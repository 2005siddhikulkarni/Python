def main():
    iValue1 = 0
    iValue2 = 0

    print("Enter the first number: ")
    iValue1 = int(input())

    print("Enter the second number: ")
    iValue2 = int(input())

    if(iValue1 > iValue2):
        print("Maximum is: ",iValue1)

    else:
        print("Maximum is: ",iValue2)

if __name__ == "__main__":
    main()