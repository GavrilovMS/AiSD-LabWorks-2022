import Stack
import Queue

str_in = input().split()

operator_stack = Stack.Stack()
output_Queue = Queue.Queue()

operators = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 2}
functions = ["cos", "sin"]

for i in range(0, str_in.__len__()):
    token = str_in[i]

    if token in functions:
        operator_stack.push_back(token)

    elif token in operators.keys():
        if operator_stack.getsize() != 0:
            while operator_stack.last() in operators.keys() and operators[operator_stack.last()] >= operators[token]:
                cur_op = operator_stack.pop_back()
                output_Queue.enqueue(cur_op)
        operator_stack.push_back(token)

    elif token == "(":
        operator_stack.push_back(token)

    elif token == ")":
        while operator_stack.last() != "(":
            cur_op = operator_stack.pop_back()
            output_Queue.enqueue(cur_op)
        operator_stack.pop_back()
        if operator_stack.last() in functions:
            cur_op = operator_stack.pop_back()
            output_Queue.enqueue(cur_op)
    else:
        output_Queue.enqueue(token)

while operator_stack.getsize() != 0:
    output_Queue.enqueue(operator_stack.pop_back())

print(output_Queue)



