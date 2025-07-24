#**Recursion**

#Recursion is a programming technique where a function calls itself to solve a problem. It is often used to break down complex problems into simpler subproblems.

#**Key Concepts:**
# Base case: The condition under which the recursion stops. It prevents infinite recursion.
    #Think of it like Russian dolls where each doll contains a smaller one til you hit the smallest doll.
        #In recursion the base case would be the smallest doll, or the case where the function stops calling itself.
        #In recursion you basically traverse til you hit the base case, then you start returning back up the stack of function calls.
# Recursive case: The part of the function that includes the recursive call.
    # Think of this as the method of breaking down the problem into smaller parts.
    # This is where the function calls on itself to approach the base case. So like removing ONE doll at a time until you hit the smallest one.
# You MUST have the recursive case and base case work in tandem in order to prevent infinite recursion and to ensure the function can solve the problem.

#**Example: Factorial Function**

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)
print("Factorial Result:", factorial(5))  # Output: 120

#**Example: Infinite Loop**
def infinite_loop(n):
    if n == 0:  # Base case
        return
    else:  # Recursive case
        infinite_loop(n + 1)

#Uncomment the line below to see the infinite loop in action
# infinite_loop(1)  # This will cause a stack overflow error due to infinite recursion

#This code demonstrates the necessity for having a base case that works with the recursive case to prevent infinite recursion
