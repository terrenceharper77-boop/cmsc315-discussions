# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

While completing this assignment, I was able to gain a deeper understanding on the differences between stacks
and queues and how these data structures enforces LIFO and FIFO operational rules. The main challenge that I faced was the 
runtime errors that were raised on pop() or dequeue() calls on empty data structures. I overcame this by using try-except 
blocks within a loop that allowed the program to catch and print the error, and continue running the program smoothly.
For an example with real world application, the undo and redo options are an example of a stack (LIFO: Last in Firs Out), only
redoing the last operation (Top) that was submitted into the stack. For Queues a printer queue will delete the oldest job (bottom) once 
the oldest print is completed. (FIFO: First In First out)