def Non_Factor_Sum(Value):
    Sum = 0

    for i in range(1,Value + 1):
        if(Value % i != 0):
            Sum += i

    return Sum

def main():
    print("Enter the number: ")
    value = int(input())

    result = Non_Factor_Sum(value) 
    print("Sum of non factors are: ",result)

if __name__ == "__main__":
    main()