# Python program to subtract two lists

# take list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 3, 4, 7, 9]

# print original list
print('list1 =', a)
print('list2 =', b)

# subtraction of list
sub = list(set(a) - set(b))

# print subtraction value
print('list1 - list2 =', sub)