def Pattern(rows,cols):
   
    for i in range(rows,0,-1):

        for j in range(1,cols + 1):
            print(i,end="\t")

        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__== "__main__":
    main()