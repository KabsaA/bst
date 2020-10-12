class Node:
    def __init__(self, data , next):
        self.data = data
        self.next = next



class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def _len(self):
        return self.size

    def is_empty(self):
        return sefl.size == 0


  #ADD something to the top of the stack
  def push(self, item):
    self.my_stack.append(item)

  #DELETE remove something from the top of the stack
  def my_pop(self):
    return self.my_stack.pop(len(self.my_stack) - 1)

  #READ the top of the stack
  def peek(self):
    return self.my_stack[len(self.my_stack) - 1]
