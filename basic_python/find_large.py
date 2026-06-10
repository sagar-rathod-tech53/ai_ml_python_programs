
# my_list = [18, 65, 20]
# new_list = sorted(my_list)
# print("Largest number:",new_list[-1])
# for i in new_list:
#     if 
#     print("All numbers: ",i)

# numbers = [19,76,49]
# Largest = numbers[0]

# for i in numbers:
#     if i > Largest:
#         Largest = i
# print("The largest number is : ",Largest)

num_length = int(input("Enter the how many degit you want: "))
lists = []
for i in range(num_length):
    val = int(input(f"Enter the value: {i} "))
    lists.append(val)
print("You entered numbers: ",lists)
largest_num = lists[0]
for j in lists:
    if j > largest_num:
        largest_num = j

print("The largest number you enter is ",largest_num)