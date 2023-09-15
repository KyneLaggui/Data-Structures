def INFIXTOPOSTFIX(userInfixExpression):
    stackList = [] 
    appendElem = "" 
    operatorsSymbol = set(["+","-","*","/","(",")","^",])
    operatorValue= {"+":1, "-":1, "*":2,"/":2, "^":3} 

    for elements in userInfixExpression:
        if elements not in operatorsSymbol: 
            appendElem = appendElem + elements

        elif elements == "(":
            stackList.append("(")

        elif elements== ")":
            while stackList and stackList [-1]!= "(":
                appendElem = appendElem + stackList.pop()
            stackList.pop()

        elif elements == ")":
            while stackList and stackList [-1]!= "(":
                appendElem = appendElem + stackList.pop()
            stackList.pop(elements)
        
        else:
            while stackList and stackList [-1]!= "(" and operatorValue[elements] <= operatorValue[stackList[-1]]:
                appendElem = appendElem + stackList.pop()
            stackList.append(elements)

    while stackList:
        appendElem = appendElem + stackList.pop()
    return appendElem

userInfixExpression = input("Enter the Infix Expression you wish to convert to Postfix Expression\nEnter the Infix Expression: ")
convertInfixToPostfix = INFIXTOPOSTFIX(userInfixExpression)
print(f"Post Expression is :: {convertInfixToPostfix}")




