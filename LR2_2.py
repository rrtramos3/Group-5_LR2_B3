def Main():    
    
    fileName = input("Enter file name: ")
    f = open(fileName, 'r').read()

    text = f.split('\n')

    while True:
        lineNumber = int(input("Enter line number to print: "))

        if lineNumber == 0:
            break
        else:
            print(text[lineNumber- 1])
            #print(strNumbers)

if __name__ == "__main__":
    Main()
