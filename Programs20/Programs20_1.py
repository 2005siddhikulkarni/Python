def Check(arr,No):

    for i in arr:
        if(i == No):
            return True
        
    return False

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

    ans = Check(arr,Value)

    if(ans == True):
        print("Number is present")

    elif(ans == False):
        print("Number is not present")

if __name__ == "__main__":
    main()