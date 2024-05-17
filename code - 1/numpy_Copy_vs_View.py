#   python3 pandas_Read_CSV.py

"""
python3 numpy_Copy_vs_View.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print("---------------------------------------------------")

x = arr.view()
arr[0] = 42

print(arr)
print(x) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x) 


print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

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


