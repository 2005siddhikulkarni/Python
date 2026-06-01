def Display(Value):
    for i in range(Value):
        print("*",end = "")

    print("\n")
    for j in range(Value):
        print("#",end = "")

def main():
    print("Enter the number: ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()