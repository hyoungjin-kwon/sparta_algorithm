s = "(())()"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        delete_head = self.head
        self.head = delete_head.next

        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"

        return self.head.data

    def is_empty(self):
        return self.head is None

def is_correct_parenthesis(string):
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push(char)
        else:
            if stack.peek() == '(':
                stack.pop()
            else:
                return False

    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))