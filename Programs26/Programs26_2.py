def CountChar(string, ch):
    cnt = 0

    for i in range(len(string)):
        if(string[i] == ch):
            cnt += 1

    return cnt
            
def main():
    print("Enter the string: ")
    String = input()

    print("Enter the character to check: ")
    ch = input()

    ans = CountChar(String, ch)
    print("The characters are: ",ans)

if __name__ == "__main__":
    main()