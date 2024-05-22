student = ["shristi","chettri"]
print(type(student))
print(len(student))
a = list(student)
print(a)
print(type(a))
a.append("hi")
print(a)
print(tuple(a))
# tuple means list[] to set()

# set
set = {1,2,3,4,1,1,3}
print(set)
print(type(set))

data = ("shristi","chettri",10)
for i in data:
    print(i)
    print(data)