def ChkCapital(ch):

    if(ch >= "A" and ch <= "Z"):
        return True
    
    else:
        return False

def main():
    print("Enter the character: ")
    ch = input()

    ans = ChkCapital(ch)

    if(ans == True):
        print("It is a capital character")

    else:
        print("It is not a capital character")

if __name__ == "__main__":
    main()