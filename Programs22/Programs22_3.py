def ChkDigit(digit):

    if(digit >= 0 and digit <= 9):
        return True
    
    else:
        return False

def main():
    print("Enter the digit: ")
    digit = int(input())

    ans = ChkDigit(digit)

    if(ans == True):
        print("It is a digit")

    else:
        print("It is not a digit")

if __name__ == "__main__":
    main()