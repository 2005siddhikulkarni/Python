def ChkChar(string, ch):

    for i in range(len(string)):
        if(string[i] == ch):
            return True
        
    return False

def main():
    print("Enter the string: ")
    String = input()

    print("Enter the character to check: ")
    ch = input()

    ans = ChkChar(String, ch)

    if(ans == True):
        print("Character found")

    else:
        print("Character not found")

if __name__ == "__main__":
    main()