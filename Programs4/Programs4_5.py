def Fact_diff(Value):
    Sum_fact = 0
    non_sum_fact = 0
    Fact_diff = 0

    for i in range(1,Value + 1):
        if(Value % i == 0):
            Sum_fact += i

        else:
            non_sum_fact += i

    Fact_diff = Sum_fact - non_sum_fact

    return Fact_diff
    
def main():
    print("Enter the number: ")
    value = int(input())

    result = Fact_diff(value) 
    print("Factorial difference is: ",result)

if __name__ == "__main__":
    main()