#   python3 pandas_Read_CSV.py

"""
python3 numpy_Searching_Arrays.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) 


print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

print("---------------------------------------------------")

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

print("---------------------------------------------------")

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

print("---------------------------------------------------")

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x) 

print("---------------------------------------------------")


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


