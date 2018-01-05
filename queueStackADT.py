

from dataStructures import Queue
import check

# Implementation of the Stack ADT using a single Queue.
class Stack:
    '''
    Stack ADT
    '''
    
    ## Stack () produces an empty stack.
    ## __init__: None -> Stack
    def __init__(self):
        self.stack = Queue ()

    ## isEmpty(self) returns True if the Stack is empty, False otherwise
    ## isEmpty: Stack -> Bool
    def isEmpty(self):
        return self.stack.isEmpty ()

    ## len(self) returns the number of items in the stack.
    ## __len__: Stack -> Int
    def __len__(self):
        return self.stack.__len__()

    ## peek(self) returns a reference to the top item of the Stack without 
    ## removing it. Can only be done on when Stack is not empty and does
    ## not modify the stack contents.
    ## peek: Stack -> Any
    ## Requires: Stack cannot be empty
    def peek(self):
        assert len(self.stack) > 0, "Cannot peek from empty Stack"
        delta = len(self.stack) - 1
        while delta != 0:
            item = self.stack.dequeue()
            self.stack.enqueue(item)
            delta -= 1
        item = self.stack.dequeue()
        self.stack.enqueue(item)
        return item

    ## pop(self) removes and returns the top (most recent) item of the Stack,
    ## if the Stack is not empty. The next (2nd most recent) item on the
    ## Stack becomes the new top item.
    ## pop: Stack -> Any
    ## Requires: Stack cannot be empty
    ## Effects: The next (2nd most recent) item on the Stack becomes the new
    ## top item.
    def pop(self):
        assert len(self.stack) > 0, "Cannot pop from Empty Stack."
        delta = len(self.stack) - 1
        while delta != 0:
            item = self.stack.dequeue()
            self.stack.enqueue(item)
            delta -= 1
        return self.stack.dequeue()

    ## push(self,item) adds the given item to the top of the Stack
    ## push: Stack Any -> None 
    ## Effects: adds the given item to the top of the Stack
    def push(self, item):
        self.stack.enqueue(item)
        
    ## print(self) prints the items in the Stack (for testing purposes)
    ## __str__: Stack -> Str
    ## Requires: Stack cannot be empty
    def __str__(self):
        assert not self.isEmpty(), "Cannot print from an empty Stack."
        return self.stack.__str__()
    
## Test
t1 = Stack()
check.expect("Q1T1",t1.isEmpty(),True)
check.expect("Q1T2",len(t1),0)

t1.push(1)
check.expect("Q1T3",t1.isEmpty(),False)
check.expect("Q1T4",t1.peek(),1)
check.expect("Q1T5",len(t1),1)


t1.push(100)
check.expect("Q1T6",t1.isEmpty(),False)
check.expect("Q1T7",t1.peek(),100)
check.expect("Q1T8",len(t1),2)

check.expect("Q1Ta",t1.pop(),100)
check.expect("Q1T9",t1.isEmpty(),False)
check.expect("Q1T10",t1.peek(),1)
check.expect("Q1T11",len(t1),1)

check.expect("Q1Tb",t1.pop(),1)
check.expect("Q1T12",t1.isEmpty(),True)
check.expect("Q1T13",len(t1),0)

