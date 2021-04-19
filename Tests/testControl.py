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

# retrive All tests From firebase
def getTests():
    testInfos = []
    allTests = database.child('test').get().val()
    testKeys = natsort.natsorted(allTests.keys(), reverse=True)
    testData = OrderedDict((k, allTests[k]) for k in testKeys)
    for testKey in testKeys:
        testInfo = testData[testKey]
        testInfos.append(testInfo)
    return testInfos

# createTest accepting testInfo from view
def createTest(testInfo):
    testKey = "test" + str(testInfo['testId'])
    database.child('test').child(testKey).set(testInfo)

# updateTest 
def updateTest(test, testId):
    testKey = "test" + str(testId)
    database.child("test").child(testKey).update(test)

# Delete Test From database
def deleteTest(test,testId):
    testKey = "test" + str(testId)
    database.child("test").child(testKey).remove()

