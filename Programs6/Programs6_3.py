def Table(No):

    for i in range(1,11):
        print(i * No)
    
def main():
    print("Enter the number: ")
    Value = int(input())

    Table(Value)

if __name__ == "__main__":
    main()