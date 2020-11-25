# Создаем класс Track
class Track():
    # Инициализруем атрибуты
    def __init__(self, name='', duration=0):
        # Имя песни
        self.name = name
        # Длина песни
        self.duration = duration

    def show(self):
        # Получаем информацию по конкретной песне
        return f' {self.name} : {self.duration} min'


# Создаем класс Album
class Album:
    # Инициализируем атрибуты класса
    def __init__(self, author, name):
        # Имя альбома
        self.name = name
        # Имя автора
        self.author = author
        # Хранилище треков
        self.tracks = []

    def add_track(self, track):
        # Добавляем треки в хранилище
        self.tracks.append(track)

    def get_tracks(self):
        # Выводим список всех имен песен
        return [track.show() for track in self.tracks]

    def get_duration(self):
        # Считаем продолжительность всех песен альбома
        res = 0
        for track in self.tracks:
            res += track.duration
        return res


# Создаем пустой массив для альбомов
albums = []

# Создаем экземпляр альбома №1
album = Album('The Prodigy', 'The Fat of The Land')

# Добавляем название треков и их продолжительность в альбом
album.add_track(Track('Firestarter', 4))
album.add_track(Track('No Man Army', 5))
album.add_track(Track('Breath', 6))
albums.append(album)

# Создаем экземпляр альбома №2
album = Album('Zodiac', 'Disco Alliance')

# Добавляем название треков и их продолжительность в альбом
album.add_track(Track('Zodiac', 5))
album.add_track(Track('Pacific', 4))
album.add_track(Track('Alliance', 3))
albums.append(album)

# Выводим информацию по альбомам и трекам
for album in albums:
    print(f'Исполнитель: "{album.author}"\nАльбом: "{album.name}"')
    for track in enumerate(album.get_tracks(), 1):
        print(f'{track[0]}.{track[1]}')
    print(f'Длительность всех треков: {album.get_duration()} минут\n')
