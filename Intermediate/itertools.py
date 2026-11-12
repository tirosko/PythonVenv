# itertools: prodct, permutations, combinations, accumulate, groupby, and infinite iterators
# https://youtu.be/HGOBQPFzWKo?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t=5826

# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/itertools.html#itertools.product
# https://docs.python.org/3/library/itertools.html#itertools.permutations
# https://docs.python.org/3/library/itertools.html#itertools.combinations
# https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement

# from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a, b)
# print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]
# prod = product(a, b, repeat=2)
# print(list(prod))  # [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]
#
# https://youtu.be/HGOBQPFzWKo?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t=6002
# from itertools import permutations
# a = [1, 2, 3]
# perm = permutations(a)
# # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# print(list(perm))

# https://youtu.be/HGOBQPFzWKo?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t=6161
# from itertools import combinations, combinations_with_replacement, groupby, count, cycle, repeat
# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# comb = combinations(a, 3)
# print(list(comb))  # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
# comb_wr = combinations_with_replacement(a, 2)
# # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
# print(list(comb_wr))
#
# from itertools import accumulate
# a = [1, 2, 3, 4]
# acc = accumulate(a)
# print(a)
# print(list(acc))

# acc = accumulate(a, func=lambda x, y: x * y)
# print(list(acc))  # [1, 2, 6, 24]
# ---------------------------------------------------------------------------------------------------
# from itertools import groupby
# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
#            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
# # groupby is used to group the data based on the key function


# def smaller_than_3(x):
#     return x < 3


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# group_obj = groupby(a, key=smaller_than_3)
# # group_obj = groupby(a, key=lambda x: x < 3)
# for key, group in group_obj:
#     print(key, list(group))  # True [1, 2] False [3, 4, 5, 6, 7, 8, 9]

# group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value))
# -------------------------------------------------------------------------------------
# from itertools import count, cycle, repeat

# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# a = [1, 2, 3]
# count = 0
# for i in cycle(a):
#     count += 1
#     print(i)
#     if count == 9:
#         break

# for i in repeat(1, 4):
#     print(i)
