def Product(arr,len):
    product = 1

    if(arr == None or len <= 0):
        return -1

    for i in range(len):
        if(arr[i] % 2 != 0):
           product *= arr[i]

    return product
    
def main():
    print("Enter the number to enter in array: ")
    Nos = int(input())

    arr = []

    print("Enter the numbers: ")

    for i in range(Nos):
        i = int(input())
        arr.append(i)

    ans = Product(arr,Nos)
    print("Product of odd numbers is: ",ans)

if __name__ == "__main__":
    main()