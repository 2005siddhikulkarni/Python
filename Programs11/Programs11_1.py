def PrintAlphabet(Value):
    ch = "A"

    for i in range(1,Value + 1):
        print(ch)
        ch = chr(ord(ch) + 1)

def main():
    print("ENetr the number: ")
    No = int(input())

    PrintAlphabet(No)

if __name__ == "__main__":
    main()