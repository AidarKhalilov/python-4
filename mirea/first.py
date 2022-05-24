from MyDictionary import MyDictionary


d = MyDictionary()
d["1"] = 2
d[2] = set()
d[3.5] = "12345"
print(d[2], d[3.5], d["1"])
for el in d:
    print(el)
# assert dict() == MyDictionary()
d2 = dict()
d2["1"] = 2
d2[2] = set()
d2[3.5] = "12345"
assert d["1"] == d2["1"]
assert d[2] == d2[2]
assert d[3.5] == d2[3.5]