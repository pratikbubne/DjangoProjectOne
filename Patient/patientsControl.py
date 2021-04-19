import pyrebase
import natsort
from collections import OrderedDict

firebaseConfig = {
    'apiKey': "AIzaSyAQDbpFM_xCUFb4beA-WnnmdeF9Qr0nznw",
    'authDomain': "parikshanlab-bb0b1.firebaseapp.com",
    'databaseURL': "https://parikshanlab-bb0b1.firebaseio.com",
    'projectId': "parikshanlab-bb0b1",
    'storageBucket': "parikshanlab-bb0b1.appspot.com",
    'messagingSenderId': "1097749011886",
    'appId': "1:1097749011886:web:6e5e8154d7f618f4e87c3f",
    'measurementId': "G-NDLBBLT7FF"
  }
# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

# It will retrive Patient By Its ID 
def getPatientById(patientId):
    try:
        patientData = database.child('patient').order_by_child('patientId').equal_to(str(patientId)).get().val()
    except:
        patientData = database.child('patient').order_by_child('patientId').equal_to(int(patientId)).get().val()
    patientKey = list(patientData.keys())[0]
    patientInfo = patientData[patientKey]
    return patientInfo

# It will retrive All Patient From Firebase
def getPatients():
    patientInfos = []
    allPatients = database.child('patient').get().val()
    patientKeys = natsort.natsorted(allPatients.keys(), reverse=True)
    patientData = OrderedDict((k, allPatients[k]) for k in patientKeys)
    for patientKey in patientKeys:
        patientInfo = patientData[patientKey]
        patientInfos.append(patientInfo)
    return patientInfos

def getUserById(userId):
    try:
        userData = database.child('user').order_by_child('userId').equal_to(str(userId)).get().val()
    except:
        userData = database.child('user').order_by_child('userId').equal_to(int(userId)).get().val()
    userKey = list(userData.keys())[0]
    userInfo = userData[userKey]
    return userInfo

def updatePatient(patient, patientId):
    patientKey = "patient" + str(patientId)
    database.child("patient").child(patientKey).update(patient)