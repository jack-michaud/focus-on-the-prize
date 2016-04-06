import requests
import json
from bs4 import BeautifulSoup as bs

class ASDFocusAPI:

	def __init__(self, username, password):
		self.BASE_URL = 'https://focus.asdnh.org/focus/'
		self.API_URL = 'API/APIEndpoint.php'
		self.SESSION = requests.session()
		data = {
			'login': 'true',
			"data": "username={}&password={}".format(username, password)
		}
		r = self.SESSION.post(self.BASE_URL, data=data)
		response = json.loads(r.text)

	def retrieve_course_history(self):
		pass
		# self.SESSION.get(self.BASE_URL + self.API_URL)

	def get_schedule(self):
		url = self.BASE_URL + 'Modules.php?modname=Scheduling/Schedule.php'
		response = self.SESSION.get(url)
		soup = bs(response.text, 'html.parser')

		class_table = soup.find('table', attrs={"class":"lo_table"})

		return self.dictify_table(class_table)

	def dictify_table(self, table):

		headers = []
		table_header = table.find('thead').find('tr')
		for td in table_header.find_all('td'):
			headers.append(td.string)

		classes = []
		for tr in table.find('tbody').find_all('tr'):
			index = 0
			_class = {}
			for td in tr.find_all('td'):
				_class[headers[index]] = td.string
				index += 1
			classes.append(_class)

		return classes


# Testing

api = ASDFocusAPI('<username>', '<password>')
print api.get_schedule()




