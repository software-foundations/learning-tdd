

class Person:
	def __init__(self, name: str, last_name: str, age: int) -> None:
		self.name: str = name
		self.last_name: str = last_name
		self.age: int = age

	def say_sthg(self) -> None:
		print(f'{self.name} {self.last_name} is saying hello')