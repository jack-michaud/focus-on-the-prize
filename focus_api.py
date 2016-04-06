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
		import pdb; pdb.set_trace()  # breakpoint 49ea3914 //


	def session(self):
		return self.SESSION

	def retrieve_course_history(self):
		sess = self.session()
		cookies = sess.cookies
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded',
		}
		data = 'accessID=167&api=finalGrades&method=requestGrades&modname=Grades%2FStudentRCGrades.php&arguments%5B%5D=-1&arguments%5B1%5D%5B**FIRST-REQUEST**%5D=true&arguments%5B2%5D=null&signature=d400df66f3ce479081b5a534ff42a4990b4d56c7'
		# url = '{}{}'.format(self.BASE_URL, self.API_URL)
		url = 'https://focus.asdnh.org/focus/API/APIEndpoint.php'

		response = requests.post('https://focus.asdnh.org/focus/API/APIEndpoint.php', cookies=cookies, data=data, headers=headers)
		print response.text
		return None

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
print api.retrieve_course_history()
