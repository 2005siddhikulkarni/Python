def MultipleDisplay(Value):

    for i in range(1,Value + 1):
        print(i * Value)

def main():
    print("Enter the number: ")
    Value = int(input())

    MultipleDisplay(Value)

if __name__ == "__main__":
    main()