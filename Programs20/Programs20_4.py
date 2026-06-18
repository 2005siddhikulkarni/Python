def Range(arr,len,start,end):

    if(arr == None or len <= 0):
        return -1

    print("The numbers in between are: ")
    for i in range(len):
        if(arr[i] >= start and arr[i] < end):
            print(arr[i])
    
def main():
    print("Enter the number to enter in array: ")
    Nos = int(input())

    print("Enter the number as start: ")
    start = int(input())

    print("Enter the number as end: ")
    end = int(input())

    arr = []

    print("Enter the numbers: ")

    for i in range(Nos):
        i = int(input())
        arr.append(i)

    Range(arr,Nos,start,end)

if __name__ == "__main__":
    main()