def pattern(Value):

    for i in range(Value):
        print("$")
        print("*")

def main():
    print("Enter the number: ")
    Value = int(input())

    pattern(Value)

if __name__ == "__main__":
    main()