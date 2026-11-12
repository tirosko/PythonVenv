# --------------------------------------------------------------------------------------
# Lambda funkcie sú anonymné funkcie, ktoré môžu mať ľubovoľný počet argumentov, ale môžu mať iba jeden výraz.
# Často sa používajú ako skratka na definovanie malých funkcií, ktoré sa nepoužívajú inde v kóde.
# Lambda funkcie sa definujú pomocou kľúčového slova lambda, za ktorým nasleduje zoznam argumentov, dvojbodka a výraz, ktorý sa má vyhodnotiť.
# Bežne sa používajú vo funkcionálnom programovaní, napríklad s funkciami map(), filter() a reduce().
# Lambda funkcie môžu byť užitočné na vytváranie malých, jednorazových funkcií, ktoré nie sú potrebné inde v kóde.
# Môžu sa tiež použiť na vytváranie jednoduchých funkcií, ktoré sa odovzdávajú ako argumenty vyššieho rádu funkciám, ako sú sort() alebo filter().
# Avšak, môžu tiež znížiť čitateľnosť kódu, ak sa používajú nadmerne alebo nevhodne.
# Vo všeobecnosti sa odporúča používať pomenované funkcie pre zložitejšiu logiku alebo keď sa funkcia bude používať na viacerých miestach.
# Celkovo sú lambda funkcie v Pythone mocným nástrojom, ktorý môže pomôcť urobiť kód stručnejším a výstižnejším, ale mali by sa používať rozumne na zachovanie čitateľnosti a prehľadnosti.
# --------------------------------------------------------------------------------------
# def add10(x): return x + 10


# print(add10(5))


# def add10_func(x):
#     return x + 10


# print(add10_func(5))

# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D)

# print(points2D)
# print(points2D_sorted)
# # [(1, 2), (5, -1), (10, 4), (15, 1)]
# print(sorted(points2D, key=lambda x: x[0]))
# print(sorted(points2D, key=lambda x: x[1]))

# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x*2, a)
# print("----------")
# print(a)
# print(list(b))

# # filter(func, seq)
# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x: x % 2 == 0, a)
# print("----------")
# print(a)
# print(list(b))
# c = [x for x in a if x % 2 == 0]
# print(c)
# ---------------------------------------------------------------------------
# reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4]

product_a = reduce(lambda x, y: x*y, a)
print(product_a)
#   24
