import my_stack 

def is_parentheses_matched(expression):

    #brackets = ["(", ")", "[", "]", "{", "}"]
    front_brackets = ["(", "[", "{"]
    back_brackets = [")", "]", "}"]

    parentheses = my_stack.Stack()

    for char in expression:

        if char in front_brackets:
            parentheses.push(char)

        elif char in back_brackets:

            front = parentheses.pop()
            if front == None or front_brackets.index(front) != back_brackets.index(char):
                return False

    return parentheses.empty()


