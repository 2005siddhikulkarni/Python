def Check(arr):
    
    for i in arr:
        if(i == 11):
            return True

        else:
            return False
        
def main():
    print("Enter the number of elements to enter: ")
    no = int(input())

    arr = []

    print("Enter the elements: ")
    for i in range(no):
        i = int(input())
        arr.append(i)

    ans = Check(arr)
    print("Answer is: ",ans)

if __name__ == "__main__":
    main()