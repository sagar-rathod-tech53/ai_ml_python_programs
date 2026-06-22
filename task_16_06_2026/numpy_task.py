import numpy as np

print("Version of the numpy :: ",np.__version__)

print("Creating list :: \n")

list1 = [1,2,3]
print("Printing array :: ",list1)
arr_llist1 = np.array(list1)
print("creating array using list :: ",arr_llist1)
print("Type of the array list",type(arr_llist1))
print("Numbers of dimension",arr_llist1.ndim)


#numpy array attributes
arr1 = np.array([[1,2,3],[4,5,6]])
print("numpy array :: ",arr1)

print("Shape:: ",arr1.shape)
print("Shape:: ",arr1.size)
print("Shape:: ",arr1.dtype)
print("Shape:: ",arr1.ndim)


#Array initialization methods
zero_arr = np.zeros((2,3))
print("")


# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print("Dot operation :: ",np.dot(a,b))