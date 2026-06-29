def StrCopy(src):
    dest = " "

    for ch in src:
        dest += ch

    return dest

def main():
    print("Enter the string: ")
    string = input()

    dest = StrCopy(string)
    print("The copied string from one string into another is: ",dest)

if __name__ == "__main__":
    main()