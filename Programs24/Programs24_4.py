def ChkVowel(string):

    for i in range(len(string)):

        if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] =="u"):
           return True
        
        else:
            return False
    
def main():
    print("Enter the string: ")
    string = input()

    ans = ChkVowel(string)
   
    if(ans == True):
        print("String contains vowel")

    else:
        print("String doesn't contains vowel")

if __name__ == "__main__":
    main()