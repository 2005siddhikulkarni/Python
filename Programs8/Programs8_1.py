import math

def CircleArea(radius):

    Area = math.pi * (radius ** 2)

    return Area

def main():
    print("Enter the radius: ")
    radius = int(input())

    result = CircleArea(radius)
    print("Area of circle is: ",result)

if __name__ == "__main__":
    main()