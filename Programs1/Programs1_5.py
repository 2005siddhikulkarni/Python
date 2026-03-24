def PrintPattern(value):
    for i in range(value):
        print("*")

def main():
    print("Enter the number: ")
    no = int(input())

    PrintPattern(no)

if __name__ == "__main__":
    main()