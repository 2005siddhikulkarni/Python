def SquareMeter(Value):
    area = 0.0929

    ans = Value * area
   
    return ans

def main():
    print("Enter the area in square feet: ")
    No = int(input())

    result = SquareMeter(No)
    print("The answer is: ",result)

if __name__ == "__main__":
    main()