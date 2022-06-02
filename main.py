from flask import *
import pyrebase
import os

app = Flask(__name__)
config = {
    "apiKey": "AIzaSyDmxEmmpzd9HNUpjwY4gFoGIzf2quEFYPo",
    "authDomain": "portifolio-13ae9.firebaseapp.com",
    "databaseURL": "https://portifolio-13ae9-default-rtdb.firebaseio.com/",
    "storageBucket": "portifolio-13ae9.appspot.com",
    "messagingSenderId": "992540015473",
    "appId": "1:992540015473:web:b25e65a7bbaf329fe3d4d0",
    "measurementId": "G-Y3W35ZXZBN"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app.secret_key = 'A1_445T_@!jhf5gH'
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        try:
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            message = request.form["message"]
            contact = {"name": name, "email": email, "subject": subject, "message": message}
            db.child("users").push(contact)
            flash("Message Successfully posted.I'll get back to you shortly. Thank you!!")
            return redirect("/")
        except:

            flash('Did not save to database')
    else:
        flash('Something went wrong. Try again!')



if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
