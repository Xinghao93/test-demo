from pythonds import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.isEmpty():
                '''
                说明传入的符号不是括号类型,即 大中花括号这三类括号类型
                '''
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "{[("
    closers = "}])"
    return opens.index(open) == closers.index(close)



s = "{[)}"
print(parChecker(s))
print(s)