def CountCap(string):

    cap = 0

    for i in range(len(string)):
        if(string[i] >= "A" and string[i]<= "Z"):
            cap += 1

    return cap

def main():
    print("Enter the string: ")
    string = input()

    ans = CountCap(string)
    print("Capital letters in string are: ",ans)

if __name__ == "__main__":
    main()