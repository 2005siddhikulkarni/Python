def StrConCat(src1,src2):

    ans = src1 + src2
    print(ans)

def main():
    print("Enter the first string: ")
    string1 = input()

    print("Enter the second string: ")
    string2 = input()

    StrConCat(string1,string2)
    
if __name__ == "__main__":
    main()