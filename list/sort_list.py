#Sort a list without using sort().


list = [25, 20, 32, 55,45]
sorted_list = sorted(list)
print("Sorted list is: ",sorted_list)

# max = list[0]
# list_sort = []
# for i in list:
#     print(i)
#     if i > max:
#         max = i
#         list_sort.append(max)
# print("Sorted list is: ",list_sort) 

sorted_lst = []
while list:
    min_num = min(list)
    sorted_lst.append(min_num)
    list.remove(min_num)
print("Sorted list is: ",sorted_lst)