"""
232. Implement Queue using Stacks

Understand the Question: implement standard functions of a queue (push, peek, pop, empty)using two stacks.
Can only use valid stack methods include: push, peek/pop, size, is_empty.

instructions:void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Clarifying questions:
1. Can I use a list to implement the stack?
2. Can I use a deque to implement the stack?
3. 


Brainstorm ideas:
1. push simply appends a value to one of the stacks
2. fifo characteristic of a queue would mean popping from the "bottom" of the
stack (invalid), so need a second stack that appends all the popped items
from stack one (ending in the first item being on top) and popping the last (first)
item
3.returning the top item
4. returning if both stacks are empty

"""
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x:int) -> bool:
        while len(self.stack2)> 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)


    def pop(self) -> int:
        if not self.stack2:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        last_item = self.stack2.pop()
        print(last_item)
        return last_item
    
    def peek(self) -> int:
        if not self.stack2:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        print(self.stack2[-1])
        return self.stack2[-1]
    
    def empty(self) -> bool:
        print(len(self.stack1) == 0 and len(self.stack2) == 0)
        return len(self.stack1) == 0 and len(self.stack2) == 0
    

    def print_queue(self) -> list[int]:
        if not self.stack2:
            return self.stack1

        if not self.stack1:
            return list(reversed(self.stack2))

    def get_length(self) ->int:
        if not self.stack2:
            return len(self.stack1)

        if not self.stack1:
            return len(list(reversed(self.stack2)))



obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
param_3 = obj.peek()
print(obj.print_queue())
param_4 = obj.empty()    

assert param_2 == 2
assert param_3 == 3
assert obj.print_queue() == [3, 4, 5]
assert obj.get_length() == 3
assert param_4 == False
print("All tests passed!")