#sets

#membership string
n={"mohith","tarak","venkatesh"}
print("venkatesh" in n)#true
print("gopal" not in n)#true

#union

set1 = {1,2,3}
set2 = {3,4,5}
result = set1 | set2 
print(result)#{1,2,3, 4, 5}

#intersection

set1 = {1,2,3}
set2 = {3,2,4,5}
result = set1 & set2 
print(result) #{2, 3}

#difference
set1 = {1,2,3,6,7,8}
set2 = {3,2,4,5}
result = set1 - set2 
print(result)#{8, 1, 6, 7}

# Symmetric Difference
set1 = {1,2,3,6,7,8}
set2 = {3,2,4,5}
result = set1 ^ set2 
print(result)#{1, 4, 5, 6, 7, 8}

# Subset
set1 = {1,2,3,6,7,8}
set2 = {1,2,3,6,7,8,9}
result = set1 <= set2 
print(result)#True

#superset

set1 = {1,2,3,6,7,8,9}
set2 = {1,2,3,6,7,8}
result = set1 >= set2
print(result)#True

# Disjoint Sets
set1 = {1,2,3}
set2 = {6,7,8}
result = set1.isdisjoint(set2)
print(result)#True

#built in methods
set1 = {1,2,3}
set1.add(5)
print(set1)#set1 = {1,2,3,}

set1.remove(3)
print(set1)#{1, 2, 5}

set1.discard(5)
print(set1)#{1,2}

set1 = {1,2,3,6,7,8,9}
set1.pop()
print(set1)#{2, 3, 6, 7, 8, 9}
set1.pop()
print(set1)#{3, 6, 7, 8, 9}

set1.clear()
print(set1)#set()

set1 = {1,2,3,6,7,8}
set2 = {6,7,8}
print(set1.union(set2))#{1, 2, 3, 6, 7, 8}

print(set1.intersection(set2))#{8, 6, 7}

print(set1.difference(set2))#{1, 2, 3}

print(set1.symmetric_difference(set2))#{1, 2, 3}

set1.update(set2)
print(set1)#{1, 2, 3, 6, 7, 8}

set1.intersection_update(set2)
print(set1)#{8, 6, 7}

set1.difference_update(set2)
print(set1)#set()

set1.symmetric_difference_update(set2)
print(set1)#{8, 6, 7}

set3=set2.copy()
print(set3)#{8, 6, 7}

print(set1.isdisjoint(set2))#False

print(set1.issubset(set2))#True

print(set1.issuperset(set2))#True

#Built in Functions

set1 = {1,2,3,6,7,8,22,33,4,5,66}

print(len(set1))#11

print(max(set1))#66

print(min(set1))#1

print(sum(set1))#157

print(sorted(set1))#[1, 2, 3, 4, 5, 6, 7, 8, 22, 33, 66]

set3="mohith","tarak","gopal"

print(set3)#('mohith', 'tarak', 'gopal')
#frozen set

tarak=frozenset([1,2,3])
print(tarak) #frozenset({1, 2, 3})













