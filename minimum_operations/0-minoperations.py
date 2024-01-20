#!/usr/bin/python3

  """minimum operations."""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 2
        current_length += clipboard

    return operations

# Test cases
n1 = 4
print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

n2 = 12
print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))

