point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point ["z"] = 20
print(point)
if "a" in point:
    print(poin["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key, value in point.items():
    print(key, value)