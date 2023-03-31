items = [
    ("product1", 12),
    ("product2", 9),
    ("product3", 10),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
