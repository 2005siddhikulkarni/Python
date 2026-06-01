def OddFactorial(Value):
   Fact = 1

   for i in range(1,Value + 1,2):
       Fact *= i
       return Fact
       
def main():
    print("Enter the number: ")
    Value = int(input())

    ans = OddFactorial(Value)
    print("Odd factorial is: ",ans)

if __name__ == "__main__":
    main()