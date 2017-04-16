import googlemaps
import pyowm

def directions(ad1, ad2):
	#set up googlemaps
	k = '<YOUR GOOGLE API KEY>'
	gmaps = googlemaps.Client(key = k)

	#init
	directions = ''

	#get raw directions
	raw_directions = gmaps.directions(ad1, ad2)

	#parse raw directions
	for j in range(0, len(raw_directions[0]['legs'][0]['steps'])):
		#remove html <br>
		directions_split = raw_directions[0]['legs'][0]['steps'][j]['html_instructions'].split('<b>')
		directions_int = ''.join(directions_split)
		
		#remove html </br>
		directions_split = directions_int.split('</b>')
		for s in directions_split:
			if s.find('<') != -1:
				directions_split.remove(s)

		#contstruct directions
		directions = directions + str(j + 1) + '. ' + ''.join(directions_split) + '\n'

	#return
	return('DIRECTIONS >>>\n' + directions)

def weather(ad1):
	#set up open weather
	owm = pyowm.OWM('<YOUR PYOWM KEY>')
		
	#get weather data
	weather = owm.weather_at_place(ad1)
	w = weather.get_weather();
	temp = w.get_temperature(unit = 'celsius')

	#return
	return('WEATHER >>>\n' + 'Status: ' + str(w.get_status()) + '\nTemp (*C): ' + str(round(temp['temp'], 2)))

def forecast(ad1):
	#set up open weather
	owm = pyowm.OWM('<YOUR PYOWM KEY>')
		
	#get weather data
	forecast = owm.daily_forecast(ad1)
	weathers = forecast.get_forecast().get_weathers()
	w = weathers[0]
	temp_data = w.get_temperature(unit = 'celsius')
	temp = (temp_data['min'] + temp_data['max']) / 2

	#return
	return('FORECAST >>>\n' + 'Status: ' + str(w.get_status()) + '\nTemp (*C): ' + str(round(temp, 2)))