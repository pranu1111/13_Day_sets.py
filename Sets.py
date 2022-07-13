myset={'g','k','o','c',11}
# print(type(myset))

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# print("c" in myset)

myset.add("p")
# print(myset)
myset.add("s")
# print(myset)
sets={"prani","rani","soni","shivani"}

# myset.update(sets)
# print(myset)  
# myset.remove("shivani")
# print(myset)

# myset.remove("o")
# print(myset)
# myset.remove("k")
# print(myset)
# myset.remove("g")
# print(myset)

sets=sets.union(myset)
# print(sets)
sets.update(myset)
# print(sets)

s1={"n","x","k",1.11,58,18,10,"o","r"}
s2={1.11,18,"l","x","k",10,44,33,86,"pinkey"}

# s1.intersection_update(s2)
# print(s1)
# s1=s1.intersection(s2)
# print(s1)

# s1.symmetric_difference(s2)
# print(s1)
s1.pop()
print(s1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)
# z=s1.difference(s2)
# print(z)

s2.discard("pinkey")
print(s2)