import pyrebase

firebaseConfig = {'apiKey': "AIzaSyAolNZOEp0GwtmLxF-9SL3iIFfVWrL24y0",
    'authDomain': "trader-d966e.firebaseapp.com",
    'databaseURL': "https://trader-d966e-default-rtdb.firebaseio.com",
    'projectId': "trader-d966e",
    'storageBucket': "trader-d966e.appspot.com",
    'messagingSenderId': "508194482318",
    'appId': "1:508194482318:web:8388ccefc99462c8ab01df",
    'measurementId': "G-1T57360YWB"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# create db connection
db = firebase.database()
# create auth connection
# auth = firebase.auth()
# # create storage connection
# storage = firebase.storage()

# push data

man = 'name'
employment = 'self_employment'

data={'age':40, 'address':"Georgia", employment:'true', man:'Rahm El'}
db.push(data)

