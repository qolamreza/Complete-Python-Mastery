items = [
    ("product1", 12),
    ("product2", 9),
    ("product3", 10),
]


items.sort(key=lambda item: item[1])
print(items)
