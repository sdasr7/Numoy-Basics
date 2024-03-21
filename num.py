""" Numpy Basics ----> Supriyo Das """

import numpy as np

# Single Dimension Array
a = np.array([1, 2, 3])
print("Single Dimension Array:")
print(a)
print()

# Multi Dimension Array
b = np.array([(1, 2, 3), (5, 6, 7)])
print("Multi Dimension Array:")
print(b)
print()

# Accessing elements
print("Accessing elements:")
print("First row:", b[0])  # Output: [1, 2, 3]
print("Second row:", b[1])  # Output: [5, 6, 7]
print("Element at index [1, 1]:", b[1][1])  # Output: 6
print()

# NumPy Operations
print("NumPy Operations:")
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (4, 5, 6)])
print("Number of dimensions in 'a':", a.ndim)  # Output: 1
print("Number of dimensions in 'b':", b.ndim)  # Output: 2
print("Byte size of each element in 'a':", a.itemsize)  # Output: 4
print("Data type of 'a':", a.dtype)  # Output: int32
print("Reshaped 'b':")
print(b.reshape(3, 2))
print()

# Size and shape
print("Size and Shape:")
a = np.array([(1, 2, 3, 4, 5, 6)])
b = np.array([(1, 2, 3), (4, 5, 6)])
print("Size of 'a':", a.size)  # Output: 6
print("Shape of 'a':", a.shape)  # Output: (1, 6)
print("Shape of 'b':", b.shape)  # Output: (2, 3)
print()

# Slicing
print("Slicing:")
a = np.array([(1, 2), (3, 4), (5, 6)])
print("Array 'a':")
print(a)
print("First row:", a[0])  # Output: [1, 2]
print("Third row:", a[2])  # Output: [5, 6]
print("Element at index [3, 1]:", a[2, 1])  # Output: 6
print()

# MIN/MAX
print("MIN/MAX:")
a = np.array([1, 2, 5])
print("Minimum value:", a.min())  # Output: 1
print("Maximum value:", a.max())  # Output: 5
print("Sum of all elements:", a.sum())  # Output: 8
print()

# linspace
print("linspace:")
print("Default linspace(2, 10):", np.linspace(2, 10))
print("linspace(2, 10, 5):", np.linspace(2, 10, 5))
print("linspace(2, 10, 9):", np.linspace(2, 10, 9))
print()

# zeros and ones
print("zeros and ones:")
print("Array of zeros:", np.zeros(5))
print("Array of ones:", np.ones(5))
print()

# Sum along axis
print("Sum along axis:")
a = np.array([(1, 2, 3), (3, 4, 5)])
print("Array 'a':")
print(a)
print("Sum along axis 0:", a.sum(axis=0))  # Output: [4, 6, 8]
print("Sum along axis 1:", a.sum(axis=1))  # Output: [6, 12]
print()

# Mathematical operations
print("Mathematical operations:")
a = np.array([(4), (2)])
print("Square root of 'a':", np.sqrt(a))  # Output: [2. 1.41421356]
a = np.array([(2, 4, 9), (10, 15, 20)])
print("Square root of 'a':")
print(np.sqrt(a))
print()

x = np.array([(6, 5, 8), (9, 5, 7)])
y = np.array([(1, 2, 3), (1, 2, 3)])
print("Addition:")
print(x + y)
print("Subtraction:")
print(x - y)
print("Multiplication:")
print(x * y)
print("Division:")
print(x / y)
print()

# Vertical & Horizontal Stacking
print("Vertical & Horizontal Stacking:")
x = np.array([(1, 2, 3), (4, 5, 6)])
y = np.array([(7, 8, 9), (10, 11, 12)])
print("Vertical Stack:")
print(np.vstack((x, y)))
print("Horizontal Stack:")
print(np.hstack((x, y)))
print()

# ravel
print("ravel:")
a = np.array([(1, 2, 3), (4, 5, 6)])
print("Array 'a':")
print(a)
print("ravel 'a':", np.ravel(a))
