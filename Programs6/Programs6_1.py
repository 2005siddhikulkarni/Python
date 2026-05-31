def number(No):
    if(No <= 50):
        print("Small")

    elif(No > 50 and No < 100):
        print("Medium")

    elif(No >= 100):
        print("Large")

def main():
    print("Enter the number: ")
    Value = int(input())

    number(Value)

if __name__ == "__main__":
    main()