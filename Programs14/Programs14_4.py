def Pattern(row, col):
    ch = "a"

    for i in range(1,row + 1):
        for j in range(i, i+ row):

            print(j,end = "\t")           

        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__ == "__main__":
    main()