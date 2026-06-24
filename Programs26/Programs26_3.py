def FirstChar(string, ch):

    for i in range(len(string)):
        if(string[i] == ch):
            return i
            
def main():
    print("Enter the string: ")
    String = input()

    print("Enter the character to check: ")
    ch = input()

    ans = FirstChar(String, ch)
    print("The first occurence is: ",ans)

if __name__ == "__main__":
    main()