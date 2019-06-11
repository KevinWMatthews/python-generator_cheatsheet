def iterable_function():
    for i in range(1, 10):
        if i > 3:
            return
        yield i

for item in iterable_function():
    print(item)
