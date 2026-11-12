def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()

for i in g:
    print(i)
