from flask import Flask, render_template, url_for, request, redirect, session, flash, Blueprint
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

db = firestore.client()

# pyrebase init
# Your web app's Firebase configuration

firebaseConfig = {
    'apiKey': "",
    'authDomain': "",
    'databaseURL': "",
    'projectId': "",
    'storageBucket': "",
    'messagingSenderId': "",
    'appId': "",
    'measurementId': ""
  }
 

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

teacher = Blueprint('teacher', __name__, static_folder='static', template_folder='templates')

@teacher.route('/login', methods=['GET'])
def login():
  if request.method == 'GET':
    return render_template('student-login.html')