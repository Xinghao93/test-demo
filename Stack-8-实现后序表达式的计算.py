from pythonds import Stack
'''
要先判断该表达式是不是后序表达式，需添加错误检测

'''
def postfixEval(postfixExpr):
    operandStack = Stack()
    res = 0
    tokenList = postfixExpr.split()
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand_2 = operandStack.pop()
            operand_1 = operandStack.pop()
            res = doMath(token, operand_1, operand_2)
            operandStack.push(res)

    return operandStack.pop()

def doMath(op,op1,op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


a = postfixEval("1 9 6 / +")
print(a)