def ChkCh(ch):

    if(ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z"):
        return True
    
    else:
        return False

def main():
    print("Enter the character: ")
    ch = input()

    ans = ChkCh(ch)

    if(ans == True):
        print("It is a character")

    else:
        print("It is not a character")

if __name__ == "__main__":
    main()