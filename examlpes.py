# ## Задача №2 "Аудиоколлекция"
# Необходимо уметь хранить информацию по альбомам и трекам в них. Это можно сделать, используя классы **Album** и **Track**.

# У класса **Track** есть поля:
# - Название;
# - Длительность в минутах(используется тип данных **int**).
# - И метод **show**, выводящий информацию по треку в виде *<Название-Длительность>*.

# У класса **Album** есть поля:
# - Название альбома
# - Группа
# - Список треков

# И три метода:
# - **get_tracks** - выводит информацию по всем трекам(используется метод *show*).
# - **add_track** - добавление нового трека в список треков.
# - **get_duration** - выводит длительность всего альбома.

# ## Задание:
# Создать 2 альбома с 3 треками. Для каждого вывести его длительность.



# Примерная схема такова:
# 1. Руками записать кортежи с треками в список, а также кортежи с альбомами в другой список.
# 2. Переопределить метод вывода на печать для класса треков.
# 3. Создать цикл, в котором инициировать экземпляр альбома, после чего во вложенном цикле инициировать экземпляры треков, закидывая их в список треков альбома.
# 4. По окончанию вложенного цикла вывести на печать каждый элемент списка треков.
# Схема примерная, повторяю. Возможно, что в итоговом принте требуется нечто другое. Может быть общая длительность альбома. (edited) 


# ============================
# Создаем класс Album
class Album:
    # Инициализируем атрибуты класса
    def __init__(self, name, author):
        # Хранилище для имен песен в альбоме
        self.data = []
        # Хранилище для времени песен
        self.duration = []
        # Имя альбома
        self.name = name
        # Имя автора
        self.author = author
    
    def rename(self, track):
        track.name = input('введите трек: ')
        track.duration = input('введите длину: ')


    def add_track(self, track):
        # Добавляем в хранилище имен - имя песни
        self.data.append(track.name)
        # Добавляем в хранилище времени - длину песни
        self.duration.append(track.duration)

    def get_tracks(self):
        # Выводим список всех имен песен
        return self.data

    def get_album_info(self):
        # Выводим имя альбома
        return self.name, self.author

    def get_duration(self):
        # Считаем время всех песен альбома
        result = 0
        for track_duration in self.duration:
            result += track_duration
        return round(result, 2)

# Создаем класс Track
class Track():
    # Инициализруем атрибуты
    def __init__(self, name, duration):
        # Имя песни
        self.name = name
        # Длина песни
        self.duration = duration

    # def get_info(self):
    def show(self):
        # Получаем информацию по конкретной песне
        return self.name, self.duration


# Создаем первые три песни
song1 = Track('Firestarter', 4)
song2 = Track('No Man Army', 5)
song3 = Track('Breath', 6)
# Создаем вторые три песни
song4 = Track('Zodiac', 5)
song5 = Track('Pacific', 4)
song6 = Track('Alliance', 3)
# Создаем два альбома
album1 = Album('The Fat of The Land', 'The Prodigy')
album2 = Album('Disco Alliance', 'Zodiac')
# Добавляем песни в первый альбом
album1.add_track(song1)
album1.add_track(song2)
album1.add_track(song3)
# Добавляем песни во второй альбом
album2.add_track(song4)
album2.add_track(song5)
album2.add_track(song6)

# album1.rename(name)
# print(track.show())

# Выводим информацию по альбомам
print(f'Album: "{album1.get_album_info()}". Tracks: {album1.get_tracks()} \
Длительность всех треков: {album1.get_duration()} минут')
print(f'Album: "{album2.get_album_info()}". Tracks: {album2.get_tracks()} \
Длительность всех треков: {album2.get_duration()} минут')







# class Track():
#     def __init__(self, track_name, track_length=0):
#         self.track_name = track_name
#         self.track_length = track_length

#     def show(self):
#         print(f'{self.track_name} : {self.track_length}')

# track_info = [('track1', 190), ('track2', 250), ('track3', 210)]


# class Album:
#     tracklist = []

#     def __init__(self, album_name, group_name):
#         self.album_name = album_name
#         self.group_name = group_name

#     def add_track(self, track):
#         print(self.tracklist.append(Track))

#     def get_duration(self):
#         pass
#         # print(f'Длина альбома {self.album_name}= {self.duration}')

#     def get_tracks(self):
#         pass

#     # def __str__(self):
#     #     printable_tracklist = ''
#     #     for track in self.tracklist:
#     #         printable_tracklist += ('\t' + track.__str__() + '\n')
#     #     return f'Album name: \"{self.name}\" \nAlbum author: \"{self.band}\"\nTracks: \n{printable_tracklist}'

# track_list = [('45', 'Кино'), ('Today', 'Junkie XL')]
# track_info = [('track1', 190), ('track2', 250), ('track3', 210)]


# album1 = Album(track_list)
# print(album1)

# temp = []
# for track in range(1,len(track_list)):
#     temp.append(Album(track))
#     print(temp)

# for x in range(1,len(track_list)):
#       myArray.append(myClass())

# for x in range(1,10):
#       myArray.append(0)
#   myArray[-1] = myClass

# =========================================

# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
    
#     def __repr__(self):
#         return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)

# class Circle:
#     def __init__(self, radius):
#         self.raduis = radius

#     def __repr__(self):
#         return "Circle(%.1f)" % self.raduis

#     @classmethod
#     def from_rectangle(cls, rectangle):
#         radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
#         return cls(radius)

# def main():
#     rectangle = Rectangle(3, 4)
#     print(rectangle)

#     first_circle = Circle(1)
#     print(first_circle)

#     second_circle = Circle.from_rectangle(rectangle)
#     print(second_circle)


# =================================================
# class Track:
#     def __init__(self, track_name, track_length):
#         self.track_name = track_name
#         self.track_length = track_length
    
#     def __repr__(self):
#         return f'track {self.track_name} : {self.track_length}'


# class Album:
#     def __init__(self, track):
#         self.track = track

#     def __repr__(self):
#         return "Album, {self.track}"

#     @classmethod
#     def from_track(cls, track_name, track_length):
#         return cls(track_name), cls(track_length)

# def main():
#     track1 = Track('abc', 345)
#     print(track1)

#     first_track = Album(1)
#     print(first_track)

#     second_track = Album.from_track(track1, 234)
#     print(second_track)

# main()

# ====================================
# def __str__(self):
#     printable_tracklist = ''
#     for track in self.tracklist:
#       printable_tracklist += ('\t' + track.__str__() + '\n')
# return f'Album name: \"{self.name}\" \nAlbum author: \"{self.band}\"\nTracks: \n{printable_tracklist}'



class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Person(object):
    _registry = []

    def __init__(self, name):
        self._registry.append(self)
        self.name = name

p = Person('John')
p2 = Person('Mary')
for personobject in Person:
    print(personobject)


class test:
    def __repr__(self):
        return 'object!'

print([test() for x in range(10)])


# class Person(object):
#     _registry = []

#     def __init__(self, name):
#         self._registry.append(self)
#         self.name = name

# for p in Person._registry:
#     print p



