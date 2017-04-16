import imaplib
import email
import smtplib

class mailman():
	#constructor
	def __init__ (self, adr, pas):
		self.adr = adr
		self.pas = pas

		#connect to server
		self.mail = imaplib.IMAP4_SSL('imap.gmail.com')

		#login
		self.mail.login(self.adr, self.pas)
		self.mail.list()

	#returns latest unread mail
	def check_mail(self):
		#open inbox
		self.mail.select("inbox")

		#check for unread messages
		result, data = self.mail.search(None, "UNSEEN")

		#if there are undread messages...
		if data != [b'']:

			#parse the message to a string
			ids = data[0]
			id_list = ids.split()
			latest_email_id = id_list[-1]
			result, data = self.mail.fetch(latest_email_id, "(RFC822)")
			raw_email = data[0][1]
			raw_email = raw_email.decode('utf-8')
			message = email.message_from_string(raw_email)

			return(message)
			
		return(None)

	#sends mail
	def send_mail(self, to, resp):
		#connect to server
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()

		#login
		server.login(self.adr, self.pas)

		#send resp
		server.sendmail(self.adr, to, resp)