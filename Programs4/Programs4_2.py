def Reverse_Factor(Value):
    for i in range(Value,0,-1):
        if(Value % i == 0):
            print(i)

def main():
    print("Enter the number: ")
    value = int(input())

    Reverse_Factor(value) 

if __name__ == "__main__":
    main()