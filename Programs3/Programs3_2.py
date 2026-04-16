def DisplayFactors(Value):
    if(Value < 0):
        Value = -Value

    print("The factors of",Value,"are : ")

    for i in range(1,Value+1):
        if(Value % i == 0):
            print(i, end = " ")

def main():

    print("Enter the number: ")
    Value = int(input())

    DisplayFactors(Value)

if __name__ == "__main__":
    main()