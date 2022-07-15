
first_list = ["abcd", 147, 2.43, "Tom", 74.8]

print("complete list are: ", first_list)

print("The first element of list:", first_list[0])

print("Elements starting from 2nd till 3rd: ", first_list[2:4])

print("Print elements starting from 3rd element: ", first_list[3:])

print("The total length of the list: ", len(first_list))


small_list = [222, "Tom"]

print("complete list are: ", small_list)

total = small_list*2
print("same list in  2 times: ", total)

third_list = first_list + small_list

print("The  concatenated two lists are: " + str(third_list))

sub = list(set(first_list) - set(small_list))
print("Subtract a List from Another List: ", sub)
