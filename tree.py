#Anthony Gandini

def main():
    x = eval(input("Enter the height you want the tree to be: "))
    i = int(x)
    count = .5
    whiteSpace = " "
    if(x > 0):
        while(i > 0):
            print(i * whiteSpace , int((count * 2)) * "#")
            count = count + 1
            i = i - 1
    else:
        print("\nThat number was invalid, please enter a positive integer. \n")
        main()
    print(int((x)) * whiteSpace , "#")

main()