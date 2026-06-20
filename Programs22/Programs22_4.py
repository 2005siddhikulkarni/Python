def ChkSmall(ch):

    if(ch >= "a" and ch <= "z"):
        return True
    
    else:
        return False

def main():
    print("Enter the character: ")
    ch = input()

    ans = ChkSmall(ch)

    if(ans == True):
        print("It is a small character")

    else:
        print("It is not a small character")

if __name__ == "__main__":
    main()