def StrNCopy(src,no):
    dest = " "

    for ch in src:
        if(no == 0):
            break
        dest += ch
        no -= 1

    return dest

def main():
    print("Enter the string: ")
    string = input()

    print("Enter the number: ")
    n= int(input())

    dest = StrNCopy(string,n)
    print("The copied string from one string into another is: ",dest)

if __name__ == "__main__":
    main()