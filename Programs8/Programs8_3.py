def KMToMeter(Value):
    m = 1000

    ans = Value * m
   
    return ans

def main():
    print("Enter the number in KM: ")
    No = int(input())

    result = KMToMeter(No)
    print(No,"KM is: ",result,'meters')

if __name__ == "__main__":
    main()