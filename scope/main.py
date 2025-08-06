"""
top level of a module
global scope
Scope is implemented as dictionary
"""
total_global = 5

print(globals()) # now contains 'total_global': 5

"""
LEGB rule to resolve scope
- local
- enclosing
- global
- built-in
"""

def print_total():
    """
    local scope created by function
    """
    total = 0
    print(f"From function: {total=}")


print_total()


"""
Enclosing scope
- for nested functions (inner functions)
"""

def print_with_inner():
    def inner_print_total():
        """
        Access to scope of function where is created
        """
        print(f"From inner function {total=} )")

    total = 10
    inner_print_total()
    print(f"From function {total=}")


print_with_inner()

"""
Global scope
- top scope
- only one
- all scopes can access to global scope
"""
super_global_total = 100


x = 5

def foo():
    global x # affects global variable
    x = 999
    print(x)
    
foo()
print(x)