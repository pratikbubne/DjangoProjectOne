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
storage = firebase.storage()

# retrive All Visit from Firebase
def getVisits():
    visitInfos = []
    allVisits = database.child('visit').get().val()
    if allVisits is None:
        return allVisits
    else:
        visitKeys = natsort.natsorted(allVisits.keys(), reverse=True)
        visitData = OrderedDict((k, allVisits[k]) for k in visitKeys)
        for visitKey in list(visitData.keys()):
            visitInfo = visitData[visitKey]
            visitInfos.append(visitInfo)
        return visitInfos

# retrive Visit By Visit Id
def getVisitById(visitId):
    try:
        visitData = database.child('visit').order_by_child('visitId').equal_to(str(visitId)).get().val()
    except:
        visitData = database.child('visit').order_by_child('visitId').equal_to(int(visitId)).get().val()
    visitKey = list(visitData.keys())[0]
    visitInfo = visitData[visitKey]
    return visitInfo

# createVisit by accepting visitInfo from view
def createVisit(visitInfo):
    visitKey = "visit" + str(visitInfo['visitId'])
    print("visitKey= ", visitKey)
    print("visitInfo is", visitInfo)
    database.child('visit').child(visitKey).set(visitInfo)

