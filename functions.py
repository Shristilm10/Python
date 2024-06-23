def test():
    print("i am function")
test()
test()

def multiplication (number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
num = int(input("Enter a number: "))
multiplication(num)

def hello():
    sum = 0
    a = [1,2,3]
    for i in a:
        sum = sum + i
    return sum
hello()

# positional arugements
def test(address):
    print("hello coders from", address)
test("nepal")   

def test(address,prov):
    print("hello coders from", address,prov)
test("nepal","damak")   

# default argument
def test(city,address="Nepal"):
    print("hello coders from", address)
test("damak")   

def info(fname,lname):
    print(f'my name is {fname} {lname}')
info("chettri","shristi")
info("shristi","chettri")

# keyword argument
def info(fname,lname):
    print(f'my name is {fname} {lname}')
info(lname = "chettri",fname = "shristi")
info(fname = "shristi",lname = "chettri")

# arbitrary positional arguments
def sum(*data):
    sum = 0
    return data
print(sum(1,2,3))
# output (1,2,3)

def sum(*data):
    sum = 0
    for i in data:
        sum = sum + 1
        return sum
print(sum(1,2,3))
# output 1

def sum(*data):
    sum = 0
    for i in data:
        sum = sum + 1
    return sum
print(sum(1,2,3))
# output-1+2+3=6

# keyword argument
def info(**data):
    print(data)
    print(f'my name is {data['fname']} {data['lname']}')

info(lname = "chettri",fname = "shristi")
info(fname = "shristi",lname = "chettri",midddle = "dangi")

def random(*arbit, **kargu):
    print(arbit)
    print(kargu)
    print("this is function")
random(1,2,3,"shristi","tt",test="1")

def avg(args):
    length = len(args)
    sum = 0
    for i in args:
        sum = sum + i
        average=sum/length
    return average
print(avg(1,2))

# recursion
# def rec():
#     print(1)
#     rec()
# print(rec())
# output infinite 1

def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)
print(fact(5))

# lamda argument : expression (syntox of lamda)
def test(n,m):
    return n*m
test(5*6)

# this above is simple but in lamda
x=lambda n,m:n*m
x(4,5)

# if condition
gender = "m"
if gender=="m":
 print("male")
else:
 print("female")
print(x)

# but in lamda
gender = "m"
x = "male" if gender=="m" else "female"
print(x)