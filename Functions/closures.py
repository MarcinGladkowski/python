'''
Closures in Python
- functions are higher order objects: this means we can execute them, assign value to them, pass in functions,
 compare in IF statements
- module scope is global scope
- function scope is local scope
- nonlocal: allows to get variables from closure, but from not from module (global scope)
- keyword: global - set variable to module scope
'''


def sort_priority(numbers, group):
    found = False
    def helper(x):
        nonlocal found # to don't create new function
        if x in group:
            found = True # closure error
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found


numbers = [8, 1, 3, 22, 99]
group = {2 , 3, 4, 22}

found = sort_priority(numbers, group)
print(numbers)
print(found)

