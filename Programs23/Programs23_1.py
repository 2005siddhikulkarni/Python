def Display(ch):
        
        if(ch >= "A" and ch <= "Z"):
             while(ch <= "Z"):
                  print(ch, end = "\t")
                  ch = chr(ord(ch) + 1)

        if(ch >= "a" and ch <= "z"):
             while(ch >= "a"):
                  print(ch, end = "\t")
                  ch = chr(ord(ch) - 1)

def main():
    print("Enter the character: ")
    ch = input()

    Display(ch)

if __name__ == "__main__":
    main()