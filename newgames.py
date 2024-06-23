import random
randomnos = random.randint(1,10)
print("random number",randomnos)
number = int(input("guess a number"))

while(number!=randomnos):
 number = int(input("guess a number"))
 if number == randomnos:
  break

if randomnos==number:
 print("number match")