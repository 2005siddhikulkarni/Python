def FeetsToCMs(Value):

    ans = (Value - 32) * (5.0 / 9.0)
   
    return ans

def main():
    print("Enter the area in feet: ")
    No = int(input())

    result = FeetsToCMs(No)
    print(No,"Feets is: ",result,'in centimeters')

if __name__ == "__main__":
    main()