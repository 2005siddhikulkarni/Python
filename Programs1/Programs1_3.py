def printingreversenos(value):
    for i in range(value,0,-1):
        print(i)

def main():
    print("Enter the number for printing the reverse numbers from that: ")
    n = int(input())

    printingreversenos(n)

if __name__ == "__main__":
    main()