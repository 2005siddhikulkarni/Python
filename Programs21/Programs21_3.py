def Difference(arr,len):

    imax = arr[0]
    imin = arr[0]

    for i in range(len):
        if(arr[i] > imax):
            imax = arr[i]

        elif(arr[i] < imin):
            imin = arr[i]

    diff = imax - imin

    return diff

def main():
    print("Enter the number to enter in array: ")
    Value = int(input())

    arr = []

    print("Enter the elements: ")
    
    for i in range(Value):
        i = int(input())
        arr.append(i)

    ans = Difference(arr,Value)
    print("The difference between maximum element and minimum element in the array is: ",ans)

if __name__ == "__main__":
    main()