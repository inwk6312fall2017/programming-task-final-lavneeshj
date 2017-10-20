from weather import Weather
weather = Weather()

# Lookup WOEID via http://weather.yahoo.com.

lookup = weather.lookup('4177')
condition = lookup.condition()
print(condition['text'])

# Lookup via location name.

location = weather.lookup_by_location('halifax')
condition = location.condition()
print(condition['text'])

# Get weather forecasts for the upcoming days.

forecasts = location.forecast()
for forecast in forecasts:
    print(forecasts['text'])
    print(forecasts['date'])
    print(forecasts['high'])
    print(forecasts['low'])



