import secrets

a = secrets.randbelow(100)  # Random number between 0 and 99
print(a)
a1 = secrets.randbits(8)  # Random number with 8 bits (0-255)
print(a1)

mylist = list("abcdefg")
print(mylist)
b = secrets.choice(mylist)  # Random choice from the list
