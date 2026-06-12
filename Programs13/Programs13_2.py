def Pattern(rows,cols):
    
    for i in range(1,rows + 1):

        ch1 = "A"
        ch2 = "a"

        for j in range(1,cols + 1):

            if(i % 2 == 0):
                print(ch1,end = "\t")
                ch1 = chr(ord(ch1) + 1)

            else:
                print(ch2,end="\t")
                ch2 = chr(ord(ch2) + 1)
           
        print("\n")

def main():
    print("Enter the number of rows: ")
    r = int(input())

    print("Enter the number of columns: ")
    c = int(input())

    Pattern(r,c)

if __name__== "__main__":
    main()