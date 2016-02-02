from datetime import timedelta

def add_gigasecond(time):
	try:
		return time + timedelta(0, seconds=10**9)
	except TypeError:
		print "Error: Invalid Input Date"
	
