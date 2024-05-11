# number data type
# int - 10
# float - 10.12
# complex - 2+3j

a = 10
b = 10.10
print(type(a))
print(type(b))
print(isinstance(a,int))

# string
# single line string
test = 'cychmguft'
print(type(test))

# multi line spacing
test = '''
shristi
chettri
jhapa
damak
'''

word = 'shristi'
print(word.upper())
print(word.lower())
print(word.title())
print(word.isalpha()) #isalpha is for only letter or words

name = "shristi"
lastname = "chettri"

print("my name is ",name, "and lastname is",lastname)

print(f'my name is {name} and last name is {lastname}')