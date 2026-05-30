def display(Value):

    for i in range(- Value,Value + 1):
        print(i,end = "")

        if(i != Value):
            print(",",end = " ")

def main():
    print("Enter the number: ")
    Value = int(input())

    display(Value)

if __name__ == "__main__":
    main()