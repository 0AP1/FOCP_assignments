help(dict)

stock = {"apple": 20, "banana": 15, "orange": 25, "kiwi": 10}

removed_item1 = stock.popitem()
removed_item2 = stock.popitem()

print(f"Removed item 1: {removed_item1}")
print(f"Removed item 2: {removed_item2}")
print("Updated stock dictionary:", stock)
