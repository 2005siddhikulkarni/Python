def StrCopySmall(src):
    dest = " "

    for ch in src:
        if(ch >= "a" and ch <= "z"):
            dest += ch
        
    return dest

def main():
    print("Enter the string: ")
    string = input()

    dest = StrCopySmall(string)
    print("The copied string from one string into another is: ",dest)

if __name__ == "__main__":
    main()