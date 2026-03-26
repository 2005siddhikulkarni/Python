def DisplayNoWithUserFreq(no, freq):
    for i in range(freq):
        print(no)

def main():
    print("Enter the number: ")
    value = int(input())

    print("Enter the frequency: ")
    freq = int(input())

    DisplayNoWithUserFreq(value, freq)

if __name__ == "__main__":
    main()