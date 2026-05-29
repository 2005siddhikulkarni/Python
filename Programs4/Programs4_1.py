def Factor_Mult(Value):
    count = 1

    for i in range(1,Value + 1):
        if(Value % i == 0):
            count *= i

    print("Factor Multiplication is: ",count)

def main():
    print("Enter the number: ")
    Value = int(input())

    Factor_Mult(Value)

if __name__ == "__main__":
    main()