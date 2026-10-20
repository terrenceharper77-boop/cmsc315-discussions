# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

Working through this assignment enforced my learning on how Python’s __dict__works. 
Seeing an object’s instance attributes and a class’s attributes printed separately made the distinction between instance namespaces and class namespaces concrete instead of abstract. 
I also fot to practice how inheritance and super().__init__() lets a subclass extend a parent class without duplicating its setup code.

The biggest challenge was manipulating the results coming out of Vehicle.__dict__. 
Class dictionaries mix plain data (strings, booleans) with unbound function objects, and printing those functions directly just showed memory addresses instead of anything useful. 
I had to use callable() to detect which entries were methods versus data, then call the methods against a sample instance to get a real return value instead of a reference. 
On top of that, since I hadn’t touched Python in a while, a lot of this was relearning syntax and OOP conventions I’d forgotten, which slowed me down.

Compared to procedural programming, OOP groups data and behavior together, which makes code easier to extend and 
maintain — a new vehicle subclass can reuse and override existing behavior instead of rewriting it.