#Swap two no with and without a temporary variable


#without temporary veriable
a = 5
b = 9
print(f"Before Swap a : {a} and b: {b}")
a, b = b, a
print(f"After Swap a : {a} and b: {b}")

#with temporary veriable
c = 5
d = 8
print(f"Before Swap c : {c} and d: {d}")
temp = c
c = d
d = temp
print(f"After Swap c : {c} and d: {d}")