"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # look at each element while tracking its index
    for i in range(len(lst)):
        if lst[i] == target:
            return i # found the target and returned the position
    # didn't find the position after linear search
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst)-1

    while low <= high:
        # Check for middle element, if uneven round down to whole number
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid # found the target


        elif lst[mid] < target:
        # lst [mid] and elements to its left are smaller than target.
        # Throw away the left half
            low = mid +1
        else :
        # lst[mid] and elements to the right are larger than target, discard
        # everything to the right
            high = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    s_data = [2, 4, 6, 8, 10, 12, 14]
    print("Small Dataset:", s_data)


    print("\n Searching if 10 exist in dataset (True)")
    print("  Linear Search result: ", linear_search(s_data,10))
    print("  Binary search result: ", binary_search(s_data,10))


    print("\n Searching if 7 exist in dataset (False)")
    print("  Linear Search result: ", linear_search(s_data,7))
    print("  Binary search result: ", binary_search(s_data,7))
    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    l_data = list(range(0, 20000))
    print("Dataset length: ",len(l_data))

    target = 449

    start = time.perf_counter()
    linear_result = linear_search(l_data, target)
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_result = binary_search(l_data, target)
    binary_time = time.perf_counter() - start

    print(f"\n----Searching for {target}----")
    print(f"Linear search results: {linear_result}({linear_time:.6f} seconds)")
    print(f"binary search results: {binary_result}({binary_time:.6f} seconds)")

    n_inlist = 20003

    start = time.perf_counter()
    linear_result = linear_search(l_data, n_inlist)
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_result = binary_search(l_data, n_inlist)
    binary_time = time.perf_counter() - start

    print(f"\n---Searching for {n_inlist} (does not exist):---")
    print(f"Linear search result: {linear_result}  ({linear_time:.6f} seconds)")
    print(f"Binary search result: {binary_result}  ({binary_time:.6f} seconds)")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")


    print("\nEmpty list, searching for 3:")
    print("  Linear:", linear_search([], 3))   # -1
    print("  Binary:", binary_search([], 3))   # -1

    # linear best case searches the value on first try
    # binary keeps moving left until it finds the index 0. in this case
    # linear search is faster
    print("\nFirst element (2) in small dataset:")
    print("  Linear:", linear_search(s_data, 2))   # 0
    print("  Binary:", binary_search(s_data, 2))   # 0

    # linear: checks ever index for the value
    # binary: keeps moving right:It checks for an off-by-one error at the end of the list.
    # If high started at len(lst) instead of len(lst) - 1, or the loop
    # used < instead of <=, binary search could miss the last element or crash
    print("\nLast element (14) in small dataset:")
    print("  Linear:", linear_search(s_data, 14))  # 6
    print("  Binary:", binary_search(s_data, 14))  # 6



    dup_data = [1, 3, 3, 3, 5, 7]
    # value 3 appearsat indexes 1, 2, and 3.
    print("\nDuplicates: searching for 3 in", dup_data)
    print("  Linear:", linear_search(dup_data, 3))  # 1
    # Returns 1 on the first index to match because it always scans
    # left to right and stops at the first match.
    print("  Binary:", binary_search(dup_data, 3))  # 2
    #  Returns 2, which is the middle copy, not the first one.
    #  It stops as soon as mid lands on ANY matching value, so which
    #  copy it finds depends on where the halving happens to land.

if __name__ == "__main__":
    main()