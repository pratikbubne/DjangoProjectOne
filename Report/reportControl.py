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

# It will retrive All Reports from Firebase
def getReports():
    reportInfos = []
    allReports = database.child('report').get().val()
    if allReports is None:
        return allReports
    else:
        reportKeys = natsort.natsorted(allReports.keys(), reverse=True)
        reportData = OrderedDict((k, allReports[k]) for k in reportKeys)
        for reportKey in list(reportData.keys()):
            reportInfo = reportData[reportKey]
            reportInfos.append(reportInfo)
        return reportInfos

# It will retrive All Reports By Its ID
def getReportById(reportId):
    reportData = database.child('report').order_by_child('reportId').equal_to(reportId).get().val()
    reportKey = list(reportData.keys())[0]
    reportInfo = reportData[reportKey]
    return reportInfo

# It will Create New Report By Accepting reportInfo From addReportToDB view
def createReport(reportInfo):
    reportKey = "report" + str(reportInfo['reportId'])
    database.child('report').child(reportKey).set(reportInfo)

# Send the PDF File in Firebase Storage
def reportUploadTODB(reqFile, patientId, reportId):
    sc = storage.child("Reports/patientId_{}/reportId_{}/".format(patientId, reportId)+reqFile['file1'].name).put(reqFile['file1'])
    url = storage.child("Reports/patientId_{}/reportId_{}/".format(patientId, reportId)+reqFile['file1'].name).get_url(sc['downloadTokens'])
    return url
