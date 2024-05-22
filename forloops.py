# in list
a = [1,2,3,4,5,6]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(len(a))

# but in loop 
for i in a:
    print(i)

# i = 1, i<=10; i++ 
    range(1,10,1)
    print(range)

    for i in range(1,10,1):
        print(i)

for i in range(1,10,3):
        print(i)

b = [1,2,3]
for i in range(len(b)):
     print(b[i])

length = len(a)
for i in range(0,length,1):
     print(a[i])

l = [1,-1,2,0]
for i in l:
 if i%2==0:
     print('even',i)

 if i%2==1:
     print('odd',i)

 if i<0:
     print('negative',i)

 if i==0:
     print('zero',i)

a = len(l)
for i in range(a):
    if l[i]%2 == 0:
        print('even', l[i])
    else:
        print('odd', l[i])


# multiply of 2
        n = 2
        m = 3
        print(f'2 * {m} = {n*m}')


for i in range(1,3):
    for j in range(2,5):
        print(i,j)

for i in [1,2,4,5]:
    for j in range(1,5,2):
        print(i,j)

for i in [1,2,4,5]:
    for j in range(1,11,2):
        print(f'{i}*{j}={i*j}')
        print('\n')

a = []
n = int(input("how many number do you want"))
for i in range(1,n+1,1):
    num = int(input("enter a number for mult"))
    a.append(num)
for i in a:
    for j in range(1,11,1):
        print(f'{i}*{j}={i*j}')
        print('\n')

a = []
n = int(input("how many number do you want"))
for index,i in enumerate(1,n+1,1):
    num = int(input(f'enter a {index}'))
    a.append(num)
for i in a:
    for j in range(1,11,1):
        print(f'{i}*{j}={i*j}')
        print('\n')








     