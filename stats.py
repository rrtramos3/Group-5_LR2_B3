def Mean(numbers):

    sum = 0

    if len(numbers) != 0:
        for i in range(len(numbers)):
            sum +=  numbers[i]
        
        mean = sum / len(numbers)
    else:
        mean = sum

    return mean

def Median(numbers):
    
    if len(numbers) != 0:
        midpoint = len(numbers) // 2
        if midpoint == 1:
            medianKey = numbers[midpoint]
        else:
            medianKey = numbers[midpoint - 1]
    else:
        medianKey = 0


    return medianKey

def Mode(numbers):
    numberFrequency = {}

    if len(numbers) != 0:
        for word in numbers:
            number = numberFrequency.get(word, None)
            if number == None:
                # word entered for the first time
                numberFrequency[word] = 1
            else:
                # word already seen, increment its number
                numberFrequency[word] = number + 1

        theMaximum = max(numberFrequency.values())
        for key in numberFrequency:
            if numberFrequency[key] == theMaximum:
                return key
                break
    else:
        return 0
    

def Main():
    
    fileName = input("Enter file name: ")
    f = open(fileName, 'r').read()

    numbers = []
    strNumbers = f.split()
    numbers = list(map(int, strNumbers))

    numbers.sort()

    mean = Mean(numbers)
    median = Median(numbers)
    mode = Mode(numbers)

    print("The mean is: ", mean)
    print("The median is: ",median)
    print("The mode is: ", mode)

if __name__ == "__main__":
    Main()
