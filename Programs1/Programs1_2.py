
def Display(no,sentence):
    for i in range(1,no):
        print(sentence)

def main():
    print("Enter the number for how many times entered string should display: ")
    Value = int(input())

    print("Enter the string to be displayed: ")
    String = input()

    Display(Value, String)

if __name__ == "__main__":
    main()