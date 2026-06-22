def CountSmall(string):

    cap = 0

    for i in range(len(string)):
        if(string[i] >= "a" and string[i]<= "z"):
            cap += 1

    return cap

def main():
    print("Enter the string: ")
    string = input()

    ans = CountSmall(string)
    print("Small letters in string are: ",ans)

if __name__ == "__main__":
    main()