#   python3 pandas_Read_CSV.py
"""

python3 numpy_Array_Indexing.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4])

print(arr[0]) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4])

print(arr[1]) 

print("---------------------------------------------------")

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3]) 

print("---------------------------------------------------")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1]) 

print("---------------------------------------------------")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4]) 

print("---------------------------------------------------")

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

print("---------------------------------------------------")

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) 

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

