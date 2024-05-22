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