def Digits(arr,len):

    digit1 = 99
    digit2 = 999

    for i in range(len):
        if(arr[i] > digit1 and arr[i] < digit2):
            print(arr[i])
            
def main():
    print("Enter the number to enter in array: ")
    Value = int(input())

    arr = []

    print("Enter the elements: ")
    
    for i in range(Value):
        i = int(input())
        arr.append(i)

    Digits(arr,Value)

if __name__ == "__main__":
    main()