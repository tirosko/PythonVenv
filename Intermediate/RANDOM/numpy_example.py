# Musí sa nainštalovať knižnica numpy
# pip install numpy
import numpy as np

a = np.random.rand(3)
print(a)
b = np.random.rand(3, 3)
print(b)
c = np.random.randint(0, 10)
c1 = np.random.randint(0, 10, 3)
print(c)
print(c1)
d = np.random.randint(0, 10, (3, 3))
print(d)
print("--------------------------------")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)
