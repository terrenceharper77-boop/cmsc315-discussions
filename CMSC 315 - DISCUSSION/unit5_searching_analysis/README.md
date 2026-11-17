# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

One thing that really refreshed me is the difference between binary and linear search. linear search just checks elements
in sequence, O(n). Binary search dose it a little differently, it halves the search space at each comparison at O(log n).
I was also rusty at using time to code, so I had to remember how to implement time into my code. My biggest challenge was making sure  
my scopes for binary search were right. I had got to nearly the end of the assignment, and when I ran it, it went into an infinite loop.

in the code:
elif lst[mid] < target:
    # lst [mid] and elements to its left are smaller than target.
    # Throw away the left half
    low = mid +1  #<------- I initially had -1
else :
    # lst[mid] and elements to the right are larger than target, discard
    # everything to the right
    high = mid - 1 #<------- I initially had +1

initially I misunderstood the implementation and switched the +/- symbols in the binary search method. this caused it to go into an infinite
loop while running the code and not print anything past the small dataset results.
From my understanding of the pros and cons of the two search methods, I would want to use linear search when the data is small and a one-off search case
like checking a rollcall roster for a single class. You would use binary search when there is a large database, like a name
in a graduation ceremony roster. It's like a rollcall roster but it 5-6 pages of names in-order that'll take time to search. 