import csv
import json
import pyrebase



class Database:
    def __init__(self, data):
        self.data = data


    def write_to_file(self):
        with open('./database_dir/database.txt', 'a') as database_txt:
            email = self.data['email']
            subject = self.data['subject']
            message = self.data['message']
            file = database_txt.write('\n{},{},{}'.format({email},{subject},{message}))

    def wrote_to_csv(self):
        with open('./database_dir/database.csv', 'a', newline='') as database_csv:
            email = self.data['email']
            subject = self.data['subject']
            message = self.data['message']
            csv_writer = csv.writer(database_csv)
            csv_writer.writerow([email, subject, message])

    def write_to_json(self):
        with open('./database_dir/database.json', 'a') as database_json:
            file = json.dumps(self.data)
            archive = database_json.write(file)

    def firebase_database_writer(self):
        config = {
            "apiKey": "AIzaSyDmxEmmpzd9HNUpjwY4gFoGIzf2quEFYPo",
            "authDomain": "portifolio-13ae9.firebaseapp.com",
            "storageBucket": "portifolio-13ae9.appspot.com",
            "messagingSenderId": "992540015473",
            "appId": "1:992540015473:web:b25e65a7bbaf329fe3d4d0",
            "measurementId": "G-Y3W35ZXZBN"
        }
        firebase = pyrebase.initialize_app(config)
        self.firebase_database = firebase.database()
        self.firebase_database.child('users').push(self.data)