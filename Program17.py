class Demo:
    def CheckEven(iNo):

        if((iNo % 2) == 0):
            print("It is even number")
        
        else:
            print("It is odd number")

def main():
    iValue = 0

    dobj = Demo()

    print("Enter the number: ")
    iValue = int(input())

    dobj.CheckEven(iValue)

if __name__ == "__main__":
    main()