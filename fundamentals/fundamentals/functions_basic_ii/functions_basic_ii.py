#1 Countdown
def countdown(input):
    count=[]
    for x in range(0, input + 1):
        count.append(input)
        input = input - 1
    return count

#2 Print and Return
def printAndReturn(first):
    print(first[0])
    return(first[1])

#3 First Plus Length
def firstPlusLength(second):
    return second[0] + len(second)

#4 Values Greater Than Second
def valuesGreaterThanSecond(third):
    if len(third) > 1:
        newList = []
        for x in third:
            print("This is third[x]", str(x))
            if x > third[1]:
                newList.append(x)
        return newList
    else:
        return False

#5 This Length, That Length
def thisLengthThatLength(length, value):
    newList = []
    for x in range(length):
        newList.append(value)
    return newList

