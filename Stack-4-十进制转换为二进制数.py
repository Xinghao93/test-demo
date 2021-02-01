from pythonds import Stack

def divideBy2(decNumber):
    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber // 2 

    binString = ""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())
    
    return print(binString)

# test

a = 236
divideBy2(236)


