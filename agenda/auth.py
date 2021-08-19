import pyrebase
import firebase_token as token

class Login:
    def login(email, password):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email, password)
            if user:
                return True
        except Exception as e:
            print("Error"+str(e.args[1]))
            return False

    def list_all():
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            agenda = db.child('agenda').get()
            return agenda
        except Exception as e:
            print("Error"+str(e.args[0]))
            return False

    def insert(self, name, email):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            db = firebase.database()
            data = {"name":name,"email":email}
            db.child('agenda').push(data)
            return True
        except Exception as e:
            print("Error"+str(e.args[0]))
            return False