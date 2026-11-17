# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
   
It took me some time to understand the BST at the coding level, because I had to bring together concepts from 
previous weeks and see how they work in one structure. in turn, I reviewed the course work multiple times until I 
understood how each piece connected. BST places smaller values on the left and larger values on the right.
This ordering of each comparison eliminates about half of the remaining saving time compared to other data structures, 
Search and insertion take O(log n) in a balanced tree. Compared to an unsorted list and a sorted array 0(n) for sorting 
and insertion, a BST shortens search and insertion time. But if values are inserted in sorted order the tree becomes 
unbalanced,so searching it essentially no faster than searching a list, which is O(n).