def CountEven(arr):
    Cnt1 = 0
    Cnt2 = 0

    for i in arr:
        if(i % 2 == 0):
            Cnt1 += 1

        else:
            Cnt2 += 1
        
    return Cnt1 - Cnt2

def main():
    print("Enter the number of elements to enter: ")
    no = int(input())

    arr = []

    print("Enter the elements: ")
    for i in range(no):
        i = int(input())
        arr.append(i)

    ans = CountEven(arr)
    print("Count is: ",ans)

if __name__ == "__main__":
    main()