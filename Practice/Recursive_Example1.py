'''
Understand recursive function calls and implement simple recursive functions.

•A recursive computation solves a problem by using the solution to the same problem 
 with simpler inputs.
•For a recursion to terminate, there must be special cases for the simplest inputs.

•The key to finding a recursive solution is reducing the input to a simpler input for 
 the same problem.

•When designing a recursive solution, do not worry about multiple nested calls. Simply 
 focus on reducing a problem to a slightly simpler one.
'''
def reverse(s):
    # Base case: if the sequence has 0 or 1 element, it's already reversed
    if len(s) <= 1:
        return s
    
    # Recursive case: take the first element and put it at the end.
    # We use s[0:1] instead of s[0] so that it returns a sequence (list/string)
    # rather than a single element, preventing TypeErrors when adding lists.
    return reverse(s[1:]) + s[0:1]

# Example usage
print(reverse("hello"))        # → "olleh"
print(reverse("Python"))       # → "nohtyP"
print(reverse([1, 2, 3, 4]))   # → [4, 3, 2, 1]