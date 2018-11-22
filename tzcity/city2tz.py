import pickle
with open('city2timezone_data.pickle', 'rb') as handle:
    city2timezone = pickle.load(handle)
def city2tz(city):
	if city.lower() in city2timezone:
		return city2timezone[city.lower()]
	else:
		raise ValueError("Oops!  City not found.  Try again...")
		
	