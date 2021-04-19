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

def imageUploadTODB(reqFile):
    sc = storage.child("Images/"+reqFile['image'].name).put(reqFile['image'])
    url = storage.child("Images/"+reqFile['image'].name).get_url(sc['downloadTokens'])
    return url

def createOffer(offerInfo):
    offerKey = "offer" + str(offerInfo['offerId'])
    database.child('offer').child(offerKey).set(offerInfo)

def getOffers():
    offerInfos = []
    allOffers = database.child('offer').get().val()
    if allOffers is None:
        return allOffers
    else:
        offerKeys = natsort.natsorted(allOffers.keys(), reverse=True)
        offerData = OrderedDict((k, allOffers[k]) for k in offerKeys)
        for offerKey in list(offerData.keys()):
            offerInfo = offerData[offerKey]
            offerInfos.append(offerInfo)
        return offerInfos
