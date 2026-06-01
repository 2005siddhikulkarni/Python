def Factorial_Diff(Value):
   EvenFact = 1
   OddFact = 1

   for i in range(2,Value + 1,2):
       EvenFact *= i
   print(EvenFact)

   for j in range(2,Value + 1,2):
       OddFact *= j
   print(OddFact)
       
   Diff = EvenFact - OddFact

   return Diff

def main():
    print("Enter the number: ")
    Value = int(input())

    ans = Factorial_Diff(Value)
    print("Factorial is: ",ans)

if __name__ == "__main__":
    main()