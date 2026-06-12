def Pattern(rows,cols):
    
    for i in range(1,rows + 1):

        ch = "A"

        for j in range(1,cols + 1):
            print(ch,end="\t")
            ch = chr(ord(ch) + 1)

        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__== "__main__":
    main()