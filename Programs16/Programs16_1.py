def Pattern(row,col):

    for i in range(1,row + 1):
        for j in range(1, col + 1):

            if(i < j):
                print(end = "\t")

            else:
                print("*",end = "\t")

        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__ == "__main__":
    main()