from collections import Iterable
from collections import Iterator

print(isinstance([],Iterable))

isinstance({}, Iterable)
print(isinstance({}, Iterable))

isinstance('abc', Iterable)
print(isinstance('abc', Iterable))

isinstance((x for x in range(10)), Iterable)
print(isinstance((x for x in range(10)), Iterable))

isinstance(100, Iterable)
print(isinstance(100, Iterable))

print('-----------------------1')


isinstance((x for x in range(10)), Iterator)
print(isinstance((x for x in range(10)), Iterator))

isinstance([], Iterator)
print(isinstance([], Iterator))

isinstance({}, Iterator)
print(isinstance({}, Iterator))

isinstance('abc', Iterator)

print(isinstance('abc', Iterator))

print('-----------------------2')