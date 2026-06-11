def RevPattern(row,col):

    for i in range(1,row + 1):
        for j in range(col,0,-1):

            print("\t", j, end = "")

        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    RevPattern(r,c)

if __name__ == "__main__":
    main()