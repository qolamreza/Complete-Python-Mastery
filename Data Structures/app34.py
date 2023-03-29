items = [
    ("product1", 12),
    ("product2", 9),
    ("product3", 10),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

