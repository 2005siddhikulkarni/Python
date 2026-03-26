def Display(no):
    i = 0

    while(i < no):
        print("*")

        i+=1

def main():
    print("Enter the number: ")
    value = int(input())

    Display(3)

if __name__ == "__main__":
    main()