def Non_Factor(Value):
    
    for i in range(1,Value + 1):
        if(Value % i != 0):
            print(i)
    
def main():
    print("Enter the number: ")
    value = int(input())

    Non_Factor(value) 

if __name__ == "__main__":
    main()