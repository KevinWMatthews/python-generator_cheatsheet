class Iterable:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        for item in self.collection:
            yield item

collection = [7, 8, 9]
iterable = Iterable(collection)

for item in iterable:
    print(item)
