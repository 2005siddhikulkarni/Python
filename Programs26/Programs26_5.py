def RevStr(string):
    
    for i in range(len(string) - 1,-1,-1):
        print(string[i], end = "")
            
def main():
    print("Enter the string: ")
    String = input()

    RevStr(String)
    
if __name__ == "__main__":
    main()