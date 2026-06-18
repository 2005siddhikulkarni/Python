def Check(arr,len,Value):

    for i in range(1,len + 1):
        if(arr[1] == Value):
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

    ans = Check(arr,Nos,Value)

    if(ans == True):
        print("First occurence of number")

    elif(ans == False):
        print("There is no such number present")

if __name__ == "__main__":
    main()