import random

a = random. random()
print(a)

b = random.uniform(1, 10)
print(b)

c = random.randint(1, 10)  # 10 is included
print(c)

d = random.randrange(1, 10)  # 10 is not included
print(d)

e = random.normalvariate(0, 1)  # mean=0, stddev=1
print(e)

mylist = list("abcdefg")
print(mylist)
f = random.choice(mylist)
print(f)
f1 = random.choices(mylist, k=3)  # k=3 means 3 random choices
print(f1)
# k=3 means 3 random choices without replacement
f2 = random.sample(mylist, k=3)
print(f2)
f3 = random.shuffle(mylist)  # shuffle the list in place
print(mylist)

random. seed(1)
print(random.random())
print(random.randint(1, 10))
random. seed(1)
print(random.random())
print(random.randint(1, 10))
# random. seed(1) is used to initialize the random number generator with a specific seed value. This ensures that the sequence of random numbers generated is reproducible. In this case, the seed value is set to 1, which means that every time you run the code, you will get the same sequence of random numbers.
# This is useful for debugging and testing purposes, as it allows you to reproduce the same results every time you run the code.
