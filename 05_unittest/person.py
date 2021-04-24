import requests


class Person:
	def __init__(self, name: str, last_name: str, data_obtained: bool = False):
		self.name = name
		self.last_name = last_name
		self.data_obtained = data_obtained

	def get_all_data(self):
		# response = requests.get('http://jsonplaceholder.typicode.com/users/1')
		# or
		response = requests.get('')		

		if response.ok is True:
			self.data_obtained = True
			return 'CONECTED'
		else:
			self.data_obtained = False
			return 'ERROR 404'
