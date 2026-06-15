# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows + 1, 0,-1):  # Outer loop for rows
#     for j in range(1, i):  # Inner loop for columns
#         # print()   # Print star
#         print("*", end=" ")
#     # print("*", end=" ")
#     print()

# n = 5
# for i in range(n, 0, -1):
#     print("* " * i)

# for i in range(rows , 0 , -1):
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(1, 2*i):
#         print("*", end=" ")
#     print()


# for i in range(1 , rows +1):
#     for j in range(1 , i + 1):
#         if i == 1 or j == 1 or i == rows or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# count = 1
# n = 5
# for i in range(1 , n):
#     for j in range(1, i+1):
        
#         if count == 6:
#             count+=1
#             print(count," ", end="")
#             #  count-=1
#             continue
#         elif count == 7 or count == 9:
#             if count == 7:
#                 print("* ", end="")
#             elif count == 9:
#                 print("# ", end="")
#         elif count == 10:
#             count-=1
#             print(count," ", end="")
#         else:
#             print(count," ", end="")
#         count+=1
#     print()

# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()


n = 5
for i in range(1, n ):
    for k in range(n -i):
        print(" ", end="")
    for j in range(1, i+1):
        if i == 3:
            continue
        else:
            print(" *", end="")
    print()




# n = 5
# for i in range(1, n):
#     for j in range(1, i+1):
#         print("* ", end="")
#     print()

# n = 5
# count = 1
# for i in range(1, n):
#     for j in range(1, i+1):
#         if count % 2 == 0:
#             print("* ", end="")
#         else:
#             print("# ", end="")
#         count+=1
#     print()
