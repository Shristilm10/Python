a = 11

try:
    print(a+b)
except NameError:
  print("name error")
except ValueError:
  print("value error")
except ZeroDivisionError:
   print("zero error")
except:
   print("diffrent error")

#    
a = 11
b = [12,23]
try:
    for i in range[10]:
       b[1]
except NameError as e:
  print(e)
except ValueError as e:
  print(e)
except ZeroDivisionError as e:
   print(e)
except IndexError as e:
   print(e)
except:
   print("diffrent error")
