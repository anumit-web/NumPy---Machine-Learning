#   python3 pandas_Read_CSV.py
"""

python3 numpy_Array_Slicing.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) 


print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:]) 


print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4]) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2]) 

print("---------------------------------------------------")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) 

print("---------------------------------------------------")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2]) 

print("---------------------------------------------------")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4]) 

print("---------------------------------------------------")


print("---------------------------------------------------")



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

