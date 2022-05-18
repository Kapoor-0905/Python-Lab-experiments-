#Q1. 
#(a) Convert numbers =[1, 2.0, 3] to numpy array and convert all elements to string type.
#(b) Create a 2 D array through list and set dtype as int32
#(c) Find the rows and columns of the 2d array created in part b
#(d) Print 10 random numbers between 1 and 100.


import numpy as np
#(a)
arr=[1,2.0,3]
arr=np.array(arr)
arr=arr.astype(str) 
print(arr)
#(b)
arr2d=[[1,2,3],[4,5,6]]
arr2d=np.array(arr2d)
arr2d=arr2d.astype(np.int32)
print(arr2d)
print(arr2d.dtype)
#(c)
rows=arr2d.shape[0]
cols=arr2d.shape[1]
print(rows,cols)
#(d)
for i in range(10):
    print(np.random.randint(1,100))

#---------------------------------------------------------------------------------------------------------

#Q2
#a) Write a NumPy program to get help on the add function
#b) Write a NumPy program to test whether none of the elements of a given array is zero
#c) Write a NumPy program to test whether any of the elements of a given array is non-zero
#d) Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution

#(a) 
import numpy as np
print(np.info(np.add))

#(b)
arr = np.array([0,0,0,0,0,0])
check = np.all(arr==0)
if(check==True):
    print("All zero")
else:
    print("non zero element present")
#(c)
arr = np.array([0,0,0,0,0,8])
check = np.any(arr!=0)
if(check==True):
    print("non zero element present")
else:
    print(" All Zero")
#(d) 
arr = np.random.randint(1,50,15).reshape((3,5))
print(arr)
