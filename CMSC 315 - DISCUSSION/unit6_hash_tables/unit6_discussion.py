"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    grades = {}

    grades["Balake"]= 99
    grades["Alice"] = 89
    grades["Drake"] = 60
    grades["Wayne"] = 42
    grades["Cordellia"] = 100
    # Python turns each key into an identifier that points to a storage spot.
    # It goes straight to that spot, so adding items is fast.

    print("\n---Grade table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    wayne_grades = grades.get("Wayne") # if wayne wasn't ing the dictionary, None would be returned
    print(f"Wayne's grade is {wayne_grades}")

    drake_grades= grades.get("Drake")
    print(f"Drake's grade is {drake_grades}")

    alice_grade = grades["Alice"]
    print(f" Alice grade is {alice_grade}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    key = "Wayne"
    print("\n---Grade table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")
    print(f"{key}'s current grade {grades.get(key)}")
    # Wayne is already a key, so once its hashed again it'll go directly to the same spot
    # Wane's grade of 45 will eb replaced, no new entry is added so dictionary is still
    # same size
    print("\n")

    print(f"Updating {key}'s grade.......")
    print("---Grade table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")

    grades[key]=99.9
    print(f"{key}'s current grade {grades.get(key)}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    grades["temporarystudent"]= 0
    print("\n---Grades Table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")

    del grades["temporarystudent"] # python uses th key "Carmen" to find her spot,
    # then removes both the key and its value from the dictionary.
    # The dictionary gets one item smaller.
    print("\n---Grades Table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")
    # Edge case 1: Look up a missing key
    # "temporarystudent" was deleted earlier, so Python hashes the key
    # but finds nothing
    temp_grade = grades.get("temporarystudent")
    print(f"temporarystudent's grade is {temp_grade}")

    # Edge case 2: Update a missing key
    # "Marcus" isn't in the dictionary, so there's nothing to update.
    # Python adds him as a new key-value pair, and the dictionary grows by one.
    print(f"Students before: {len(grades)}")
    print("\n---Grades Table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")

    grades["Marcus"] = 75
    print(f"\nStudents after:  {len(grades)}")

    print("---Grades Table---")
    for name, grade in grades.items():
        print(f"  name: {name:<10}......{grade}")
    print(f"Marcus's grade is {grades.get('Marcus')}")



if __name__ == "__main__":
    main()