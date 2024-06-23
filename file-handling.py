# read
f = open("main.py", 'r')
print(f.read())

# read 'r' append 'a' write 'w' create 'x'

# append
f = open("aa.txt", 'a')
f.write("i am from append mode")
f.close()
f = open("aa.txt", 'r')
print(f.read())

# add data on aa.txt which is append
a = []
for i in range(1,10,1):
  a.append(i)
f = open("aa.txt", 'a')
f.write(a)
f.close()
f = open("aa.txt", 'r')
print(f.read())

# write
f = open("aa.txt", 'w')
f.write("i am write")

# to delete folder
import os
os.rmdir("folder name")