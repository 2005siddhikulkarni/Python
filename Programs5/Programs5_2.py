def display(Value):

    for i in range(1,Value + 1):
        print(i)

def main():
    print("Enter the number: ")
    Value = int(input())

    display(Value)

if __name__ == "__main__":
    main()