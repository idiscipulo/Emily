class message():
	#constructor
	def __init__ (self, string):
		self.raw = string;
		self.sender = string['From']
		self.content = ''

		#parse the raw message
		self.parse()

	#get sender
	def get_sender(self):
		return(self.sender)

	#get content
	def get_content(self):
		return(self.content)

	#parse raw into content
	def parse(self):
		#parse the string for content
		for part in self.raw.walk():
			#for Verizon
			if part.get_content_type() == 'text/plain':
				#get content
				self.content = part.get_payload().lower()
			#for AT&T
			elif part.get_content_type() == 'text/html':
				#split message string
				raw_split = part.get_payload().split()

				#find content indices
				cont_start = raw_split.index('<td>') + 1
				cont_end = raw_split.index('</td>')
					
				#construct content
				for i in range(cont_start, cont_end):
					self.content = self.content + raw_split[i] + ' '
					self.content = self.content.lower()