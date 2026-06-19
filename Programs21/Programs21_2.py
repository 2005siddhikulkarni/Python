def Minimum(arr,len):

    imin = arr[0]

    for i in range(len):
        if(arr[i] < imin):
            imin = arr[i]

    return imin

def main():
    print("Enter the number to enter in array: ")
    Value = int(input())

    arr = []

    print("Enter the elements: ")
    
    for i in range(Value):
        i = int(input())
        arr.append(i)

    ans = Minimum(arr,Value)
    print("The minimum element in the array is: ",ans)

if __name__ == "__main__":
    main()