def Pattern(rows,cols):
    num = 1
   
    for i in range(1,rows + 1):

        for j in range(1,cols + 1):
            print(num,end="\t")
            num += 1
           
        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__== "__main__":
    main()