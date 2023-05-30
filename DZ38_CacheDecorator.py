class cacher:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        items = list(kwargs.keys())
        items.sort()
        sorted_items = {i: kwargs[i] for i in items}
        key = str(sorted(args)) + str(sorted_items)
        if key in self.cache:
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value


@cacher
def funk(x):
    if x in (0, 1):
        return 1
    else:
        return x ** x


for i in range(0, 10):
    print(funk(i))

print(funk.cache)
