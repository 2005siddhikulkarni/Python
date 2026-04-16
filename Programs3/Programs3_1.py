def First_N_EvenNo(No):

    Value = 2
    
    if(Value <= 0):
        return
    
    for i in range(0,No):
        print(Value , end = " ")
        Value += 2


def main():

    print("Enter the number : ")
    No = int(input())

    First_N_EvenNo(No)

if __name__ == "__main__":
    main()



