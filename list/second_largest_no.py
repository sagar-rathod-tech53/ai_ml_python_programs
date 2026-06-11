#Find the second largest element in a list.


numbers = [98, 34, 43, 90,44]
numbers.sort(reverse=True)
second_largest_no = numbers[1]
print("Second largest number in the given list is",second_largest_no)