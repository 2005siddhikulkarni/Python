def Reverse(string):

    for ch in range(len(string) - 1,-1,-1):
        print(string[ch],end = "\t")     

def main():
    print("Enter the string: ")
    string = input()

    Reverse(string)

if __name__ == "__main__":
    main()