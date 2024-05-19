# dictionary
student = {
    "name":"chettri",
    "address":"jhapa",
    "phone":9824978576,
    "subject":["dbms","math"]
    
}
print(type(student))
print(student['name'])

print(student['subject'][1])

student['name']="messi"
print(student)

print(len(student))
print(student.keys())
print(student.values())

student.update({"number":10,'test':"test1"})
print(student)

print[student.get('name','bbb')]
# if you find name then print name if not then print bbb

del student['name']
print(student)

# del student
# print(student)
# it will delete all students lists


student.pop('address')
print(student)

student.popitem()
print(student)
