def ChkVowel(ch):
    
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        return ch

    else:
        return False

def main():

    print("Enter the character: ")
    ch = input()

    res = ChkVowel(ch)

    if(res == ch):
        print("It is Vowel")

    else:
        print("It is Consonet")

if __name__ == "__main__":
    main()