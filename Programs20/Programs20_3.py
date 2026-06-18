def LastOcc(arr,len,Value):

    if(arr == None or len <= 0):
        return -1

    for i in range(len):
        if(arr[i] == Value):
            lastindex = i
        
    return lastindex

def main():
    print("Enter the number to enter in array: ")
    Nos = int(input())

    print("Enter the number to check: ")
    Value = int(input())

    arr = []

    print("Enter the numbers: ")

    for i in range(Nos):
        i = int(input())
        arr.append(i)

    ans = LastOcc(arr,Nos,Value)

    print("The number occurred to the last index: ",ans)

if __name__ == "__main__":
    main()