def Maximum(arr,len):

    imax = arr[0]

    for i in range(len):
        if(arr[i] > imax):
            imax = arr[i]

    return imax

def main():
    print("Enter the number to enter in array: ")
    Value = int(input())

    arr = []

    print("Enter the elements: ")
    
    for i in range(Value):
        i = int(input())
        arr.append(i)

    ans = Maximum(arr,Value)
    print("The maximum element in the array is: ",ans)

if __name__ == "__main__":
    main()