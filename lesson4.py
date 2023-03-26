names = set()
print(names)

names.add("Kiril")
print(names)
names.pop()
names.add("Kiril")
names.add("Artak")
names.add("Timofei")
print(names)
names.clear()
print(names)

devices1 = {1, 2, 3, 4, 4}
devices2 = {1, 1, 2, 2}
print(devices1 & devices2)
print(devices1 ^ devices2)

print(sum(devices1 & devices2))
print(sum(devices1 ^ devices2))

print(devices1 - devices2)
devices3 = devices1.difference(devices2)
print(devices3)

devices4 = devices3.copy()
print(devices4)