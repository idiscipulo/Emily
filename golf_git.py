import functions

DIRECTION_KEYS = ['get to', 'get from', 'directions from', 'directions to']
WEATHER_KEYS = ['weather', 'weather', 'hot', 'cold', 'sunny', 'rainy', 'foggy', 'cloudy']
FUTURE_KEYS =['tomorrow', 'will', 'going']

class golf():

	#constructor
	def __init__ (self):
		self.string = ''
		self.string_list = []

	#set input
	def read(self, content):
		self.string = content
		self.string_list = content.split(' ')

	#get response
	def speak(self):
		opcode = 0

		#check keys
		for key in DIRECTION_KEYS:
			if key in self.string:
				opcode = 1
		for key in WEATHER_KEYS:
			if key in self.string:
				opcode = 2

		if opcode == 1:
			#from '' to '' phrasing
			if self.string_list.index('from') < self.string_list.index('to'):
				#get indices address 1
				ad1 = ''
				ad1_start = self.string_list.index('from') + 1
				ad1_end = self.string_list.index('to')

				#get indices adress 2
				ad2 = ''
				ad2_start = self.string_list.index('to') + 1
				ad2_end = len(self.string_list) - 1

				#get address 1
				for i in range(ad1_start, ad1_end):
					ad1 = ad1 + self.string_list[i] + ' '

				#get address 2
				for k in range(ad2_start, ad2_end):
					ad2 = ad2 + self.string_list[k] + ' '

			else:
				#get indices address 1
				ad2 = ''
				ad2_start = self.string_list.index('to') + 1
				ad2_end = self.string_list.index('from')

				#get indices adress 2
				ad1 = ''
				ad1_start = self.string_list.index('from') + 1
				ad1_end = len(self.string_list) - 1

				#get address 1
				for i in range(ad2_start, ad2_end):
					ad2 = ad2 + self.string_list[i] + ' '

				#get address 2
				for k in range(ad1_start, ad1_end):
					ad1 = ad1 + self.string_list[k] + ' '

			#get directions
			return(functions.directions(ad1, ad2))

		if opcode == 2:
			#at phrasing
			if 'at' in self.string_list:
				#get indices address 1
				ad1 = ''
				ad1_start = self.string_list.index('at') + 1
			#in phrasing
			elif 'in' in self.string_list:
				#get indices address 1
				ad1 = ''
				ad1_start = self.string_list.index('in') + 1

			ad1_end = len(self.string_list) - 1

			#get address 1
			for i in range(ad1_start, ad1_end):
				ad1 = ad1 + self.string_list[i] + ' '

			ret_value = 0

			#check future keys
			for key in FUTURE_KEYS:
				if key in self.string:
					ret_value = 1

			if ret_value == 0:
				#return
				return(functions.weather(ad1))
			elif ret_value == 1:
				#return
				return(functions.forecast(ad1))