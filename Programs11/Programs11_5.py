def PrintPattern(Value):

    for i in range(1,Value + 1):
        print("\t",i * 2)

def main():
    print("ENetr the number: ")
    No = int(input())

    PrintPattern(No)

if __name__ == "__main__":
    main()