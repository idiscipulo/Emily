import mailman as mm
import message as ms
import golf as g

adr = '<YOUR EMAIL ADDRESS>'
pas = 'M<YOUR EMAIL PASSWORD'

mail = mm.mailman(adr, pas)
golf = g.golf()

while True:
	#check for message
	new_message_string = mail.check_mail()

	#if message
	if new_message_string != None:
		#get message content
		new_message = ms.message(new_message_string)
		content = new_message.get_content()
		
		#load content to emily
		golf.read(content)

		#get response from emily
		response = golf.speak()

		if response == None:
			response = 'I\'m sorry, I don\'t understand your question'

		#print values
		print('INPUT: ' + content)
		print('OUTPUT: ' + ' '.join(response.split('\n')))

		#send
		mail.send_mail(new_message.get_sender(), response)