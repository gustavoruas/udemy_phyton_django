# tuples are immutable sequences
# sets are unordered sets of unique elements
# boleans are just True or False

# a list is represented by []
tuple_1 = ("aa","bb","cc")

print(tuple_1)
#Cannot alter a tuple element, error occurs
# tuple_1[1] = "test"
# print(tuple_1)

# sets are listed as a {}, and has no order, printing randoms the order of unique collection
sets_1 = set()
sets_1.add("aa")
sets_1.add("bb")
sets_1.add("cc")
sets_1.add("dd")
sets_1.add("ee")
print(sets_1)

# cannot add duplicate elements in a set, it does not error out
sets_1.add("aa")
print(sets_1)