
def Count(Value):
    digit = 0
    count = 0

    if(Value < 0):
        Value = -Value

    while(Value != 0):
         digit = Value % 10

         if(digit < 6):
            count += 1

         Value = Value // 10

    return count

def main():
    print("Enter the number: ")
    No = int(input())

    ans = Count(No)
    print(ans)

if __name__ == "__main__":
    main()

