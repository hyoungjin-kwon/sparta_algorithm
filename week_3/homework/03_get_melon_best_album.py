# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, play, number):
        self.items.append((key, play, number))

    def get(self, key):
        for k, v1, v2 in self.items:
            if key == k:
                return v1, v2

class LinkedDict:
    def __init__(self, num):
        self.items = []
        for i in range(num):
            self.items.append(LinkedTuple())

    def put(self, key, play, number):
        index = hash(key) % len(self.items)
        # LInkedTuple
        # [(key, play, number)]
        self.items[index].add(key, play, number)


    def get(self, key):
        index = hash(key) % len(self.items)
        # LInkedTuple
        # [(key1, play1, number1), (key2, play2, number2)]
        return self.items[index]

def get_melon_best_album(genre_array, play_array):

    plays_per_genre = {}  # {'genre':'sum_of_plays_in_genre'}
    sings_in_genre = {}  # {'genre':(play, org_number)}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in plays_per_genre:
            plays_per_genre[genre] = play
            sings_in_genre[genre] = [(play, i)]
        else:
            plays_per_genre[genre] += play
            sings_in_genre[genre].append((play, i))

    best_album = []
    genre_list = sorted(plays_per_genre.items(), key=lambda x: x[1], reverse=True)
    for key, _ in genre_list:
        play_list = sorted(sings_in_genre[key], key=lambda x: (-x[0], x[1]))
        count = 0
        while count < 2:
            best_album.append(play_list[count][1])
            count += 1


    # for genre in genre_array:
    #     if genre not in plays_per_genre:
    #         plays_per_genre[genre] = 0
    # classes = LinkedDict(len(plays_per_genre.keys()))
    #
    # for i, sing in enumerate(genre_array):
    #     classes.put(sing, play_array[i], i)
    #     plays_per_genre[sing] += play_array[i]
    #
    # best_album = []
    # genre_list = sorted(plays_per_genre.items(), key=lambda x: x[1], reverse=True)
    # for key, _ in genre_list:
    #     play_list = sorted(classes.get(key).items, key=lambda x: (-x[1], x[2]))
    #     count = 0
    #     while count < 2:
    #         best_album.append(play_list[count][2])
    #         count += 1

    return best_album


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!