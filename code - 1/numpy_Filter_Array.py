#   python3 pandas_Read_CSV.py

"""
python3 numpy_Filter_Array.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)


# print("---------------------------------------------------")

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr) 

# print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

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


