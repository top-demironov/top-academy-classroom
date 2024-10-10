

class Video:
	def __init__(self, id: int, name: str, director: str, duration: int, rented: bool = False):
		self.__id: int = id
		self.__name: str = name
		self.__director: str = director
		self.__duration: int = duration
		self.__rented: bool = rented

	@property
	def id(self):
		return self.__id

	@property
	def duration(self) -> str:
		return f'{self.__duration // 60}:{self.__duration % 60}'

	def is_rented(self) -> bool:
		return self.__rented

	def change_status(self):
		self.__rented = not self.__rented

	def __str__(self):
		return (f'{self.__id}: {self.__director} - {self.__name} '
						f'({self.duration}) - {not self.__rented}')


class VideoManager:
	def __init__(self):
		self.__videos: list[Video] = []

	def add(self, video: Video):
		self.__videos.append(video)

	def find(self, id: int) -> Video:
		for video in self.__videos:
			if video.id == id:
				return video
		raise Exception(f'Видео с id {id} не найдено')

	def rent(self, id: int):
		video = self.find(id)
		if not video.is_rented():
			video.change_status()
		else:
			raise Exception(f'Уже арендовано!')

	def bring_back(self, id: int):
		video = self.find(id)
		if video.is_rented():
			video.change_status()
		else:
			raise Exception(f'Еще не взяли в аренду')



















vm = VideoManager()

a = Video(1, 'Name1', 'lastname1', 1440)

vm.add(a)
vm.add(Video(2, 'Name2', 'lastname2', 1740))
vm.add(Video(3, 'Name3', 'lastname3', 1121))

v1 = vm.find(3)
print(v1)
v2 = vm.find(1)
print(v2)

vm.rent(2)
vm.bring_back(2)


