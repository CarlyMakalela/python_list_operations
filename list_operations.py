my_list = []

#Append the following numbers: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending elements:", my_list)

#Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

#Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending the list:", my_list)

#Remove the last element from my_list(which is 70)
my_list.pop()
print("After removing the last element:", my_list)

# Sorting my_list in ascending order
my_list.sort()
print("After sorting the list:", my_list)

# printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("The index of 30 in my_list is:", index_of_30)