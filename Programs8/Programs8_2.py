def RectArea(height,width):

    Area =  height * width

    return Area

def main():
    print("Enter the height: ")
    h = int(input())

    print("Enter the width: ")
    w = int(input())

    result = RectArea(h,w)
    print("Area of rectangle is: ",result)

if __name__ == "__main__":
    main()