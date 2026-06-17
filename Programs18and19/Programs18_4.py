def Check(arr):
    Cnt = 0

    for i in arr:
        if(i == 11):
            Cnt += 1

    return Cnt

def main():
    print("Enter the number of elements to enter: ")
    no = int(input())

    arr = []

    print("Enter the elements: ")
    for i in range(no):
        i = int(input())
        arr.append(i)

    ans = Check(arr)
    print("Count is: ",ans)

if __name__ == "__main__":
    main()