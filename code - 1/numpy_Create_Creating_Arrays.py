#   python3 pandas_Read_CSV.py
"""

python3 numpy_Create_Creating_Arrays.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

print("---------------------------------------------------")

arr = np.array((1, 2, 3, 4, 5))

print(arr) 


print("---------------------------------------------------")

arr = np.array(42)

print(arr) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print("---------------------------------------------------")

arr = np.array(
        [
            [1, 2, 3], 
            [4, 5, 6]
        ]
    )

print(arr) 

print("---------------------------------------------------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr) 

print("---------------------------------------------------")

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)



"""
x = ["apple", "banana", "cherry"] 	list 	
x = ("apple", "banana", "cherry") 	tuple
x = {"name" : "John", "age" : 36} 	dict 	
x = {"apple", "banana", "cherry"} 	set
"""

"""
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple
x = dict(name="John", age=36) 	dict 	
x = set(("apple", "banana", "cherry")) 	set
"""

