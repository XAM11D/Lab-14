# Task 1: Basic Boolean Operations
def check_truth(a, b, c):
    return (a and b) or c

# Task 2: Logical Equivalence
def logical_equivalence(a, b):
    return a == b

# Task 3: Exclusive Or (XOR)
def xor(a, b):
    return (a and not b) or (not a and b)

# Task 4: Conditional Greeting
def greet(condition):
    if condition:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

# Task 5: Nested Conditions
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"



# Task 7: Boolean Parity
def parity(number):
    binary_repr = bin(number)
    count_ones = binary_repr.count('1')
    return count_ones % 2 == 0

# Task 8: Majority Vote
def majority_vote(a, b, c):
    return sum([a, b, c]) > 1

# Task 9: Boolean Switch
def switch(condition):
    return not condition

# Task 10: Ternary Operator Simulation
def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false

# Task 11: Validate Combination
def validate(x, y, z):
    return x or (y and z)

# Task 12: Condition Chain
def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

# Task 13: Boolean Filter
def filter_true(bool_list):
    return [value for value in bool_list if value]

# Task 14: Conditional Multiplexer
def multiplexer(a, b, c, integer):
    if a:
        return integer * 2
    elif b:
        return integer * 3
    elif c:
        return integer - 5
    else:
        return integer

