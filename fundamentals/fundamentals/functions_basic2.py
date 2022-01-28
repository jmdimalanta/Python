# #Countdown
def countdown():
    for x in range(10,-1, -1):
        print(x)
print (countdown())

# #Print and Return
myList = [2,3]
def print_and_return():
    for i in range(0, len(myList)):
        print(myList[0])
        return(myList[1])
print(print_and_return())

# #First plus length
newList = [1, 2, 3, 4, 5]
def first_plus_length():
    for i in range(0, len(newList)):
        return(newList[0]+newList[4])
print(first_plus_length())

#Values greater than second
extraList = [2, 4, 3, 5, 6]
newerList = []
def greaterThan():
    for i in range(0, len(extraList)):
        if (extraList[i]) >= (extraList[1]):
            newerList.append(extraList[i])
        continue
    return(newerList)
print(greaterThan())

#This Length, That Value
def lengthValue(a,b):
    newList = [a] * b
    print (newList)
lengthValue(5,6)
