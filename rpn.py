import operator
import re

def infix_to_postfix(infix):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    infix_list = re.findall(r'[\d]+|[+|\-|*|/|(|)]', infix)
    postfix_list = []
    op_stack = []

    for token in infix_list:
        if token.isalnum():
            postfix_list.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while op_stack and prec[op_stack[-1]] >= prec[token]:
                postfix_list.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        postfix_list.append(op_stack.pop())
    return ' '.join(postfix_list)

def evaluate_rpn(postfix):
    stack = []
    operator_map = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv}
    for token in postfix.split():
        if token.isnumeric():
            stack.append(int(token))
        elif token in operator_map:
            b = stack.pop()
            a = stack.pop()
            operation = operator_map[token]
            stack.append(operation(a, b))
    return stack[0]

def evaluate_infix(infix):
    return evaluate_rpn(infix_to_postfix(infix))


while True:
    infix_expr = str(input('>>> '))
    if infix_expr == 'exit':
        break
    print(evaluate_infix(infix_expr))
