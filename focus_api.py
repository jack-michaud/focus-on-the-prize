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



# cookies = {
#     'PHPSESSID': '68a65e9e0c10c4ed47313bb33a5ac5a5',
#     'session_timeout': '1459904140',
#     'current_session': '{%22USERNAME%22:%22jack.michaud%22%2C%22UserSyear%22:%222015%22%2C%22UserSchool%22:%221%22%2C%22student_id%22:%22167%22%2C%22STAFF_ID%22:null%2C%22staff_id%22:null%2C%22UserCoursePeriod%22:null%2C%22UserMP%22:%22315%22%2C%22AJAXRequestHandler%22:null}',
# }

# headers = {
#     'Origin': 'https://focus.asdnh.org',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': '*/*',
#     'Referer': 'https://focus.asdnh.org/focus/Modules.php?modname=Grades/StudentRCGrades.php',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Connection': 'keep-alive',
# }

# data = 'accessID=167&api=finalGrades&method=requestGrades&modname=Grades%2FStudentRCGrades.php&arguments%5B%5D=-1&arguments%5B1%5D%5B**FIRST-REQUEST**%5D=true&arguments%5B2%5D=null&signature=d400df66f3ce479081b5a534ff42a4990b4d56c7'

# requests.post('https://focus.asdnh.org/focus/API/APIEndpoint.php', headers=headers, cookies=cookies, data=data)

# cookies = {
#     'PHPSESSID': '68a65e9e0c10c4ed47313bb33a5ac5a5',
#     'session_timeout': '1459904140',
#     'current_session': '{%22USERNAME%22:%22jack.michaud%22%2C%22UserSyear%22:%222015%22%2C%22UserSchool%22:%221%22%2C%22student_id%22:%22167%22%2C%22STAFF_ID%22:null%2C%22staff_id%22:null%2C%22UserCoursePeriod%22:null%2C%22UserMP%22:%22315%22%2C%22AJAXRequestHandler%22:null}',
# }

# headers = {
# 	'Content-Type': 'application/x-www-form-urlencoded',
# }
# data = 'accessID=167&api=finalGrades&method=requestGrades&modname=Grades%2FStudentRCGrades.php&arguments%5B%5D=-1&arguments%5B1%5D%5B**FIRST-REQUEST**%5D=true&arguments%5B2%5D=null&signature=d400df66f3ce479081b5a534ff42a4990b4d56c7'

# r = requests.post('https://focus.asdnh.org/focus/API/APIEndpoint.php', headers=headers, cookies=cookies, data=data)



# cookies = {
#     'PHPSESSID': '68a65e9e0c10c4ed47313bb33a5ac5a5',
#     'session_timeout': '1459904140',
#     'current_session': '{%22USERNAME%22:%22jack.michaud%22%2C%22UserSyear%22:%222015%22%2C%22UserSchool%22:%221%22%2C%22student_id%22:%22167%22%2C%22STAFF_ID%22:null%2C%22staff_id%22:null%2C%22UserCoursePeriod%22:null%2C%22UserMP%22:%22315%22%2C%22AJAXRequestHandler%22:null}',
# }

# headers = {
#     'Origin': 'https://focus.asdnh.org',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': '*/*',
#     'Referer': 'https://focus.asdnh.org/focus/Modules.php?modname=Grades/StudentRCGrades.php',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Connection': 'keep-alive',
# }

# data = 'accessID=167&api=finalGrades&method=requestGrades&modname=Grades%2FStudentRCGrades.php&arguments%5B%5D=-1&arguments%5B1%5D%5B**FIRST-REQUEST**%5D=true&arguments%5B2%5D=null&signature=d400df66f3ce479081b5a534ff42a4990b4d56c7'

# requests.post('https://focus.asdnh.org/focus/API/APIEndpoint.php', headers=headers, cookies=cookies, data=data)

