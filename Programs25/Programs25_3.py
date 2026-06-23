def strtoggle(string):
    result = ""

    for ch in string:
        if(ch >= "a" and ch <= "z"):

            ch = chr(ord(ch) - 32)
    
        elif(ch >= "A" and ch <= "Z" ):
            ch = chr(ord(ch) + 32)

        result += ch

    return result
    
def main():
    print("Enter the string: ")
    string = input()

    ans = strtoggle(string)
    print("modified string is: ",ans)

if __name__ == "__main__":
    main()