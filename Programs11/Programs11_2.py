def PrintPattern(Value):

    for i in range(Value,0,-1):
        print("\t # \t",i)

def main():
    print("ENetr the number: ")
    No = int(input())

    PrintPattern(No)

if __name__ == "__main__":
    main()