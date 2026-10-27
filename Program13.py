def CheckEven(iNo):

    if((iNo % 2) == 0):
        return True
    
    else:
        return False

def main():
    iValue = 0
    bRet = False

    print("Enter the number: ")
    iValue = int(input())

    bRet = CheckEven(iValue)

    if(bRet == True):
        print("It is even number")

    else:
        print("It is odd number")

if __name__ == "__main__":
    main()