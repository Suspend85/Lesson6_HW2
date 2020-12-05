# Создаем класс Track
class Track():
    # Инициализруем атрибуты
    def __init__(self, name='', duration=0):
        # Имя песни
        self.name = name
        # Продолжительность песни
        self.duration = duration

    # магический метот для переопределения вывода
    def __str__(self):
        return f'{self.name} : {self.duration} min'

    # магический метод сравнения
    def __lt__(self, other):
        return self.duration < other.duration


# Создаем класс Album
class Album:
    # Инициализируем атрибуты класса
    def __init__(self, author, name):
        # Имя автора
        self.author = author
        # Имя альбома
        self.name = name
        # Хранилище треков
        self.tracks = []

    # Добавляем треки в хранилище
    def add_track(self, track):
        self.tracks.append(track)

    # магический метот для переопределения вывода
    def __str__(self):
        res = f'Author: {self.author}\nAlbum: {self.name}\nTracks:'
        for track in enumerate(self.tracks, 1):
            res += f'\n\t{track[0]}. {track[1]}'
        return res

    # Выводим список всех имен песен
    def get_tracks(self):
        return [track.__str__() for track in self.tracks]

    # Считаем продолжительность всех песен альбома
    def get_album_duration(self):
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

for album in albums:
    print(f'{album} ')
    print(f'\tTotal length: {album.get_album_duration()} min \n')

track1 = Track('Firestarter', 4)
track2 = Track('Breath', 6)
print(f'"{track1}" > "{track2}" ?\n{track1 > track2}')
