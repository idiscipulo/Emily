# Emily

### Overview
Emily is server-side software designed to allow access to common web-based services via sms messaging.

### Background
Named after the sms-based AI in Tower of God, Emily is the spritual succesor to MapChat, a program I helped develop for MLH Desert Hacks 2017. Currently the two programs perform similar functions; however, Emily has been rewritten from scratch. Starting fresh allowed me to design a more flexible architechture for Emily, supporting further growth.

### User Interface
Emily has been written to interpret "conversational" commands, although it cannot hold a conversation itself. Queries can phrased naturally, with a high likelyhood of being interpreted correctly. Responses are strictly formatted, designed to convey data as in the clearest fashion.


### Functions
Emily supports three functions (not case sensitive):

###### Directions
When given a request for directions, Emily uses the Google Maps API to attempt to generate a meaningful and accurate response. Queries must include both the starting and destination locations, but can be phrased in a variety of ways. Current accepted formats must include:
..1 "get from" LOCATION_ONE "to" LOCATION_TWO
..2 "get to" LOCATION_TWO "from" LOCATION_ONE
..3 "directions from" LOCATION_ONE "to" LOCATION_TWO
..4 "directions to" LOCATION_TWO "from" LOCATION_ONE

###### Weather
When given a request for directions, Emily uses the Python Open Weather Map API to get current weather data. Queries must include a location in question, but can be phrased in a variety of ways. Current accepted formats must include:
..1 "weather in" LOCATION_ONE
..2 "weather at" LOCATION_ONE
..3 "hot in" LOCATION_ONE
..4 "hot at" LOCATION_ONE
..5 "cold in" LOCATION_ONE
..6 "cold at" LOCATION_ONE
..7 "sunny in" LOCATION_ONE
..8 "sunny at" LOCATION_ONE
..9 "rainy in" LOCATION_ONE
..10 "rainy at" LOCATION_ONE
..11 "foggy in" LOCATION_ONE
..12 "foggy at" LOCATION_ONE
..13 "cloudy in" LOCATION_ONE
..14 "cloudy at" LOCATION_ONE

###### Forecast
When given a request for a forecast, Emily uses the Python Open Weather Map API to get weather data for the following calendar day. In addition to the accepted WEATHER formats, queries must include:
..1 "tomorrow"
..2 "will"
..3 "going"
