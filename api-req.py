# import requests

# r = requests.get(url="any url from where you need data")
# print(r)

# for x in r.json():
#     print(x['title'])
#     break

# post request 
# import requests
# test={
#     "city":"kathmandu"
# }

# r = requests.get(url="https://countriesnow.space/api/v0.1/countries/population/cities",data=test)
# print(r.text)


# ATM
a = '''
1. check balance
2. cash deposit
3. cash withdraw
'''
print(a)

balance = 0
while True:
    choice = int(input("enter a number"))
    if choice == 1:
        print("your current balance is",balance)
    
    elif choice == 2:
        money = int(input("enter a money for deposit"))
        if money<=0:
            print("deposit money")
        balance = balance + money
    
    elif choice == 3:
       money = int(input("enter a money for withdraw"))
       if balance<money:
           print("insufficient balance")
           break
       balance = balance-money
