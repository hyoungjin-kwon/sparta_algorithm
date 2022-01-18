class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # LInkedTuple
        # [(key, value)]
        self.items[index].add(key, value)


    def get(self, key):
        index = hash(key) % len(self.items)
        # LInkedTuple
        # [(key1, value1), (key2, value2)]
        return self.items[index].get(key)


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
classes = LinkedDict()

for i, sing in enumerate(range(genres)):
    classes.put(sing, plays[i])
