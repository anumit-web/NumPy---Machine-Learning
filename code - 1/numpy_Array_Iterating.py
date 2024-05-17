#   python3 pandas_Read_CSV.py

"""
python3 numpy_Array_Iterating.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3])

for x in arr:
  print(x) 

print("---------------------------------------------------")

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x) 

print("---------------------------------------------------")

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

print("---------------------------------------------------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x) 

print("---------------------------------------------------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z) 

print("---------------------------------------------------")

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x) 

print("---------------------------------------------------")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x) 

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


