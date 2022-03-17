class Stack:
 
    # Constructor to initialize the stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Function to add an element `val` to the stack
    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        # 1) Insert code here to dipslay which element is being added.
        # then add to the stack!
 
    # Function to pop a top element from the stack
    def pop(self):
        # check for stack underflow
        if self.isEmpty():
            print('Nothing in the stack!')
            exit(-1)
 
        # 2) Insert some code here to display which element is being removed.
 
        # then remove from the stack using the provided functions in this program.
       
 
    # Function to return the top element of the stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]
 
    # Function to return the size of the stack
    def size(self):
        return self.top + 1
 
    # Function to check if the stack is empty or not
    def isEmpty(self):
        return self.size() == 0
 
    # Function to check if the stack is full or not
    def isFull(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    stack = Stack(3)
 
    stack.push(1)       # Inserting 1 in the stack
    stack.push(2)       # Inserting 2 in the stack
 
    stack.pop()         # removing the top element (2)
    stack.pop()         # removing the top element (1)
 
    stack.push(3)       # Inserting 3 in the stack
 
    print('Top element is', stack.peek())
    print('The stack size is', stack.size())
 
    stack.pop()         # removing the top element (3)
 
    # check if the stack is empty
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')