def ChkEvenOdd(value):
    if( value % 2 == 0):
        return True
    
    else:
        return False

def main():
    print("Enter the number: ")
    n = int(input())

    Result = ChkEvenOdd(n)

    if(Result == True):
        print("The number is Even")

    else:
        print("The number is Odd")

if __name__ == "__main__":
    main()