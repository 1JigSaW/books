from L_stack import Stack


class Calc:

    def __init__(self, infixexpr):
        self.infixexpr = infixexpr


    def infixToPostfix(self):
        prec = {}
        prec["^"] = 4
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = Stack()
        postfixList = []
        tokenList = self.infixexpr.split()

        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                print(topToken)
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                try:
                    while (not opStack.isEmpty()) and \
                       (prec[opStack.peek()] >= prec[token]):
                          postfixList.append(opStack.pop())
                    opStack.push(token)
                except:
                    print('Введите правильную строку')

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)

    def postfixEval(self, postfixExpr):
        operandStack = Stack()
        tokenList = postfixExpr.split()

        try:
            for token in tokenList:
                if token in "0123456789":
                    operandStack.push(int(token))
                else:
                    operand2 = operandStack.pop()
                    operand1 = operandStack.pop()
                    result = doMath(token,operand1,operand2)
                    operandStack.push(result)
            return operandStack.pop()
        except:
            return 'Введите корректную строку'

    def doMath(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

res = Calc("7 * 4 + 5 * 4 ")
print(res.postfixEval(res.infixToPostfix()))