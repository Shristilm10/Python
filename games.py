import random
n = random.randint(1,14)
num = int(input("guess the number: "))
total = 1
print(n)
while(num!=n):
    num = int(input("guess the number: "))
    total = total+1
print(f'congratulation you guess on {total}time')


import random
n = random.randint(1,14)
num = int(input("guess the number: "))
total = 1
print(n)
while(num!=n):
    if total==5:
        print("guest limit")
        break
    num = int(input("guess the number: "))
    total = total+1
if num ==n:
 print(f'congratulation you guess on {total}time')