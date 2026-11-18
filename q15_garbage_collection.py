import gc
import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(self.name, "deleted")


a = [1, 2, 3]
print("Reference count:", sys.getrefcount(a))
b = a
print("Reference count after b = a:", sys.getrefcount(a))
del b
print("Reference count after del b:", sys.getrefcount(a))

print("\nNormal object")
n = Node("Node1")
del n

print("\nCircular reference")
gc.disable()
x = Node("X")
y = Node("Y")
x.other = y
y.other = x
del x
del y
print("Names deleted but objects are still in memory")
print("Collected:", gc.collect())
gc.enable()

print("\nGC settings")
print("Enabled:", gc.isenabled())
print("Threshold:", gc.get_threshold())
print("Count:", gc.get_count())

gc.set_threshold(500, 5, 5)
print("New threshold:", gc.get_threshold())
gc.set_threshold(700, 10, 10)

print("\nGC stats")
for stat in gc.get_stats():
    print(stat)
