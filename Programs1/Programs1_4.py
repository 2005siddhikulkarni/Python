def ChkDivisible(no):
    if(no % 5 == 0):
        return True
    
    else:
        return -1

def main():
    print("Enter the number: ")
    value = int(input())

    Result = ChkDivisible(value)

    if(Result == True):
        print("The number is divisible by 5")

    else:
        print("The number is not divisible by 5")

if __name__ == "__main__":
    main()
    