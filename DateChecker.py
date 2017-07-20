import pyrebase
import json
from datetime import datetime
import datetime

config = {
	"apiKey": "myKey",
	"authDomain": "thedavisconnection-92e9e.firebaseio.com",
	"databaseURL": "https://thedavisconnection-92e9e.firebaseio.com/",
	"storageBucket": "thedavisconnection-92e9e.appspot.com"
}

fb = pyrebase.initialize_app(config)
firebase = fb.database()


def stream_handler(message):
	dataDict = message["data"]
	if dataDict is not None:
		dateKeys = firebase.get().val()
		date = datetime.datetime.now().replace(microsecond=0).isoformat().replace('T', ' ')
		date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
		currentDate = str(date).replace(':' , '').replace(' ', '').replace('-', '')[:-6]
		for key in dateKeys:
			try:
				postDate = str(key).replace(':' , '').replace('-', '')[:-6]
				daysPassed = int(postDate) - int(currentDate)
				print (str(daysPassed))
				if(daysPassed >= 14 ):
					firebase.child(key).remove()
			except ValueError:
				pass

  
print ("Listening...")        
my_stream = firebase.stream(stream_handler)