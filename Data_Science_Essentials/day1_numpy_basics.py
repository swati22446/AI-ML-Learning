import numpy as np

#CREATING AN ARRAY
arr = np.array([1,2,3,4])
print(arr)

#Printing a zero matrix
nums = np.zeros((3,2)) #3 rows and 0 columns
print(nums)

# print(np.zeros())  This will give error as the brackets are empty. The shape must be assigned

#Printing ones
print(np.ones((3,2)))

#To print within a range --- (start, stop , step) --> stop value is not included & more precise for floats
print(np.arange(1 ,10, 2))

#Linespace array is one where we print non-whole numbers i.e. decimals --(start, stop , num) --> stop value is included

print(np.linspace(0, 10 ,5)) 

# MANIPULATING AN ARRAY

