def Factorial(No):

    if(No <= 0):
        No = -No

    fact = 1

    for i in range(1,No + 1):
        fact *= i
    return fact
    
def main():
    print("Enter the number: ")
    Value = int(input())

    ans = Factorial(Value)
    print("The factorial of",Value,"is: ",ans)

if __name__ == "__main__":
    main()