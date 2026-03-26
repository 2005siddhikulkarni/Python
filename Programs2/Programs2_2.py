def DisplayTxt(no):
    if(no < 10):
        print("Hello")

    else:
        print("Demo")

def main():
    print("Enter the number: ")
    value = int(input())

    DisplayTxt(value)

if __name__ == "__main__":
    main()