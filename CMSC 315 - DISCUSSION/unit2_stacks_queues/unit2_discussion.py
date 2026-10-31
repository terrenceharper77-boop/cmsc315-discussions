"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque
from logging import exception


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items= [] #initializes an empty list to store elements
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        #append() adds the value to the end of a list (top of stack)
        self.items.append(value)
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # check if stack is empty, raise error if attempting to access empty stack
        if self.is_empty():
            raise IndexError ("Error: stack is empty")

        return self.items.pop() # pop() LIFO concept removing the most recent item that was entered


    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Error: peek() attempted on empty stack")
        return self.items[-1] # index returns the items at the top of the stack without removing it, also withoiut altering the stack


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0 #true



class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        self._items = deque() #initializing an empty queue


    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # appending new incoming items to the back of the line and later removing
        # items from the front of the line ensure that older items stay at the front
        # and get processed before newer items that arrived later.
        self._items.append(value)



    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # if queue is empty raise index error exception, otherwise remove and return value at the front of the Queue
        if not self.is_empty():
            return self._items.popleft()
        raise IndexError( "deque from empty queue")


    def front(self):
        # TODO (Student): Return the front value without removing it.
        # front returns first item in the stack without removing it
        if not self.is_empty():
            return self._items[0]
        raise IndexError("peek from  an empty Queue")


    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items)==0



def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.

    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")
    print("\n=== STACK DEMO ===")

    stack =  Stack()
    print("empty stack created named: stack")

    values = [1,2,3,4]
    for value in values:
        stack.push(value)
        print((f"Pushed {value} into stack. Top of stack is now {stack.peek()}."))
    print(f"stack is now : { stack.items}")

    print("\n Popping all items (LIFO):")
    popped_list= []
    while not stack.is_empty():
        popped_list.append(stack.items[-1])
        print(f'Popped {stack.pop()}')

    print(f"items came our in reverse order: {popped_list}")

    # using while loop so that if any exceptions raise, it won't close the whole program.
    while True:

        print("\n\ndemonstration of pop() on empty stack")
        print("=== Test ===")
        try:
            stack.pop()
        except Exception as e:
            print(e) #prints the error that was caught then continues to next try block

        print("Demonstration of peek() on empty stack")
        print("=== Test ===")
        try:
            stack.peek() #attempt to peek the empty stack
        except IndexError as e:
            print(e) # prints raised error

        break #escapes the while-loop
    print("\n\n")

    # 1. Create a stack and push a single item onto it
    vstack = Stack()  # Or whatever your stack class is named
    vstack.push("Item 1")

    # 2. Remove the item using pop()
    removed_item = vstack.pop()
    print(f"Removed item: {removed_item}")

    # 3. Verify the stack is empty afterward
    # (Assuming your stack class has an is_empty() method or len() check)
    if vstack.is_empty():  # Or use: if len(vstack) == 0:
        print("Verification successful: The stack is empty.")
    else:
        print("Verification failed: The stack is not empty.")





    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    my_queue = Queue()
    print ("Created empty Queue named my_queue")

    #Adding 4 values to my_queue
    qValues = [15,24,16,99]
    for i in qValues:
        my_queue.enqueue(i)
        print(f"value {i} added to my_queue ")
    print(f"my_wueue is{my_queue._items}")

    # 4. Demonstrate FIFO (First-In, First-Out) behavior
    print("\nRemoving all items from the queue (FIFO order):")
    print(f"Dequeued: {my_queue.dequeue()} (First item added came out first)")
    print(f"Dequeued: {my_queue.dequeue()}")
    print(f"Dequeued: {my_queue.dequeue()}")
    print(f"Dequeued: {my_queue.dequeue()}")

    print("\ntest dequeuing from an empty queue.")
    print("=== Test ===")
    try:
        my_queue.dequeue()
    except Exception as e:
        print (f"Error {e}")


    print("\ntest viewing the front of an empty queue.")
    print("=== Test ===")
    try:
        my_queue.front()
    except Exception as e:
        print(f"Error {e}")

    print("\nverify a single-item queue becomes empty after removal.\n")
    single_item_queue = Queue()
    print("single_item_queue created")

    print(f"enque {99} in single items queue\n")
    single_item_queue.enqueue(99)

    print("dequeue value form single_item_queue")
    rem_value = single_item_queue.dequeue()
    print(f"removed value: {rem_value}")

    if single_item_queue.is_empty():
        print("Verification successful: The queue is empty afterward.")
    else:
        print("Verification failed: The queue is still not empty.")




if __name__ == "__main__":
    main()
