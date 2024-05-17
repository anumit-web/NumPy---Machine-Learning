#   python3 pandas_Read_CSV.py

"""
python3 numpy_Data_Types.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4])

print(arr.dtype) 


print("---------------------------------------------------")

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype) 

print("---------------------------------------------------")

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype) 

print("---------------------------------------------------")

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

print("---------------------------------------------------")

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype) 

print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


# print("---------------------------------------------------")


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


