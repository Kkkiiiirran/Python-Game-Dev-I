# Converting a list to a set

sample_list = [1,1,2,2,3,3]

sample_set = set(sample_list)

print(sample_set)

# Show that sets are not indexable
# print(sample_set[2])

# Check if an element exists in the set
if 4 in sample_set:
    print("Yes")
else:
    print("No")
    
# Adding element to the set
myset = set()
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)

# Remove the elements from the set, 

myset.remove(2)
# Throws error if element is not present
# myset.remove(5)
# Does not throw error if element is not present
myset.discard(5)

print(myset)

#Set Operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric Difference

"""
a = {1,2,3,4,5}
b = {4,5,6,7,8}

Union means addition of sets
a U b = {1,2,3,4,5,6,7,8}

Internsection means the common elements between two sets
a intersection B = {4,5}
c = {1,2,3}
d = {4,5,6}
c intersection d = None

difference of A and B is the elements that exist in A but not in B
a = {1,2,3,4,5}
b = {4,5,6,7,8}
a - b = {1,2,3}
b - a = {6,7,8}

Symmetric difference is (union of sets - intersection of sets)
a = {1,2,3,4,5}
b = {4,5,6,7,8}
a symDiff b = {1,2,3,6,7,8}

"""

a = {1,2,3,4,5}
b = {4,5,6,7,8}

# Union of Sets
print(a.union(b))
print(a | b)

# Intersection of Sets
print(a.intersection(b))
print(a & b)

# Difference of Sets
print(a.difference(b))
print(a - b)

# Symmetric Difference of Sets
print(a.symmetric_difference(b))
print(a ^ b)