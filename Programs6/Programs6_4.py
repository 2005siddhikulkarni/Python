def ReverseTable(No):

    for i in range(10,0,-1):
        print(i * No)
    
def main():
    print("Enter the number: ")
    Value = int(input())

    ReverseTable(Value)

if __name__ == "__main__":
    main()