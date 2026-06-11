#Find common elements between two lists.


list1 = [98, 34, 44, 90,44, 90]
list2 = [98, 34, 43, 90,44]

common_elements = list(set(list1) ^ set(list2))
print("Common elements between the two lists are: ", common_elements)