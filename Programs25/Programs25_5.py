def CountSpaces(string):
   count = 0

   for ch in string :
       if(ch == " "):
           count += 1

   return count

def main():
    print("Enter the string: ")
    string = input()

    ans = CountSpaces(string)
    print("Count of white spaces is: ",ans)

if __name__ == "__main__":
    main()