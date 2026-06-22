def CountDiff(string):

    cap = 0
    small = 0

    for i in range(len(string)):
        if(string[i] >= "A" and string[i]<= "Z"):
            cap += 1

        elif(string[i] >= "a" and string[i] <= "z"):
            small += 1

    diff = cap - small

    return diff
    
def main():
    print("Enter the string: ")
    string = input()

    ans = CountDiff(string)
    print("Difference between small and capital letters in string are: ",ans)

if __name__ == "__main__":
    main()