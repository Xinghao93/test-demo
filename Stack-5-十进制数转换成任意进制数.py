from pythonds import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]
    
    return newString


