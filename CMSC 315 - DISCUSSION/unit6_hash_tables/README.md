# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

In this assignment,I practiced inserting, looking up, updating, and deleting key-value pairs in a grades table.
My biggest challenge was my code crashing because I used .get() incorrectly. I then learned that using grades[key], 
when there isn't an associated key, crashes with a KeyError. While .get() safely returns None.
I fixed it by checking the syntax and using grades.get(key)so code would continue compiling.
A hash table runs each key through a hash function, which turns it into a number that points to a storage spot. 
Python jumps straight to that spot without searching every item, so inserts and lookups take O(1) time on average. 
A collision happens when two keys hash to the same spot, and Python handles it by finding another open spot.