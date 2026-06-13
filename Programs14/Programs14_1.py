def Pattern(row, col):

    num = 1
    num2 = 1

    for i in range(1,row + 1):
        for j in range(1,col + 1):

            if(num <= 9):
                print(num,end = "\t")
                num += 1

            else:
                print(num2,end = '\t')
                num2 += 1

        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__ == "__main__":
    main()