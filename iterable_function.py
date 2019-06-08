def iterate_over(collection):
    for item in collection:
        yield item

collection = [7, 8, 9]
for item in iterate_over(collection):
    print(item)
