# creating a list
list_a = [1, 2, 3]
list_b = ["aa", "bb", "cc"]
list_c = [1, 2, 3, "aa", "bb", "cc"]
list_d = [["aa", "bb", "cc"], [1, 2, 3]]


print("list length :" + str(len(list_a)))

# changing values from list
print(list_b)
list_b[1] = "cvd"
print(list_b)

# adding to the list
list_b.append("tggg")

#if adding an element list with append, it adds as nested list
#list_b.append(list_a)

#this adds each element of list A, into list B, no nested list.
list_b.extend(list_a)

print(list_b)

#TO remove the last element of list
#listb.pop(2)  #defines each of the elements to remove in the list
list_b.pop()

print(list_b)

#reverses the current order of a list
list_b.reverse()

#sorts a list
#list_b.sort()

#indexing element inside a nested list
print(list_d)
print("list_d[1][2] " + str(list_d[1][2]))

#Matrix handling
matrix_a = [[1,2,3],[4,5,6],[7,8,9]]

#Retrieving the COLUMN of the matrix - a for loop or LIST comprehension
first_col = [row[0] for row in matrix_a]

print(first_col)
