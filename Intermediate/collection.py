# from collections import Counter
# a = "aaaaabbbcccccc"
# b = Counter(a)
# print(b)
# print(b.most_common(2))
#
# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, 2)
# print(pt.x, pt.y)
# print(pt[0], pt[1])
#
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# print(ordered_dict)
# print(ordered_dict.keys())
#
# from collections import defaultdict
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d)
# # This will not raise a KeyError, but will return the default value of int(), which is 0.
# print(d['c'])
#
# https://youtu.be/HGOBQPFzWKo?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&t=5701
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([4, 5, 6])
print(d)
d.extendleft([7, 8, 9])
print(d)
d.rotate(2)
print(d)
d.rotate(-2)
print(d)
d.clear()
print(d)
