def EvenFactorial(Value):
   Fact = 1

   for i in range(2,Value + 1,2):
       Fact *= i
       return Fact
       
def main():
    print("Enter the number: ")
    Value = int(input())

    ans = EvenFactorial(Value)
    print("Even factorial is: ",ans)

if __name__ == "__main__":
    main()