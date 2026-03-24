def Division(no1,no2):
    if(no2 == 0):
        return -1
    
    else:
        Ans = no1/no2
        return Ans


def main():
    print("Enter the first number: ")
    Value1 = int(input())

    print("Enter the second number: ")
    Value2 = int(input())

    Result = Division(Value1, Value2)
    print("Division is: ",Result)

if __name__ == "__main__":
    main()