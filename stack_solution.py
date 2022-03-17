class Stack:
 
    # Constructor to initialize the stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Function to add an element `val` to the stack
    def push(self, val):
        if self.Full():
            print('Shelf is full, this is good. I am proud of you!')
            exit(-1)
 
        print(f'Hey boss I am adding {val} to the shelf.')
        self.top = self.top + 1
        self.arr[self.top] = val
 
    # Function to pop a top element from the stack
    def pop(self):
        # check for stack underflow
        if self.Empty():
            print('Oh no you did not stock the shelf, you are fired!')
            exit(-1)
 
        print(f'Customer is removing {self.peek()} from the shelf. Good job on your implementation.')
 
        # decrease stack size by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top
 
    # Function to return the top element of the stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]
 
    # Function to return the size of the stack
    def size(self):
        return self.top + 1
 
    # Function to check if the stack is empty or not
    def Empty(self):
        return self.size() == 0
 
    # Function to check if the stack is full or not
    def Full(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    stack = Stack(4)
 
    stack.push('Black Pepper 1')       # Inserting Black Pepper 1 on shelf
    stack.push('Black Pepper 2')       # Inserting Black Pepper 2 on shelf
    stack.push('Black Pepper 3')       # Inserting Black Pepper 3 on shelf
 
    stack.pop()         # removing the top element black pepper 3
    stack.pop()         # removing the top element black pepepr 2
    stack.pop()         # removing the top element black pepper 1
 
    stack.push('Black Pepper 4')       # Inserting black pepper 4 on shelf

    print('The black pepper that is in front is ', stack.peek())
    print('The amount of black pepper on the shelf is ', stack.size())
 
    stack.pop()         # removing the top element black pepper 4
 
    # check if the stack is empty
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')