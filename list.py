test = [1,2,3,"chettri"]
print(type(test))
print(test[0])
print(test[1])
print(test[2])
print(test[3])

# value of 4 and type
a = [2,3,4,5]
b = a[2]
print(f'the value is {b} and type is {type(a)}')

print(len(a))

# negative
lm = ["shristi","chettri","messi","lm","leomessi"]
print(lm[-1])

# slicing with postive indexes
lm = ["shristi","chettri","messi","lm","leomessi"]
print(lm[0:2])
print(lm[:])
print(lm[:3])
print(lm[2:])

# list method
# append
lm = ["shristi","chettri","messi","lm","leomessi"]
print("before append",lm)
lm.append("shristichettri")
print("after append",lm)

# insert
lm = ["shristi","chettri","messi","lm","leomessi"]
lm.insert(0,"index")
print(lm)

# delete
lm = ["shristi","chettri","messi","lm","leomessi"]
del lm[3]
print(lm)

# remove
lm = ["shristi","chettri","messi","leomessi"]
lm.pop
print(lm)

a = lm.pop()
print(lm)
print(a)

lm = ["shristi","chettri","messi","leomessi","messi"]
lm.remove("messi")
print(lm)

# clear
lm = ["shristi","chettri","messi","leomessi"]
lm.clear()
print(lm)

# concat
list = ["apple","mango","litchi"]
lists = ["mbappe","messi"]
newlist = list+lists
print(newlist)

# extends
list.extends(lists)
print(list)
print(lists)

