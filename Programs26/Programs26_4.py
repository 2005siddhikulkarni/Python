def LastChar(string, ch):
    cnt = 0

    for i in range(len(string)):
        if(string[i] == ch):
           Cnt = i
    
    return Cnt
            
def main():
    print("Enter the string: ")
    String = input()

    print("Enter the character to check: ")
    ch = input()

    ans = LastChar(String, ch)
    print("The last occurence is: ",ans)

if __name__ == "__main__":
    main()