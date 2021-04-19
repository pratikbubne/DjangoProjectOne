from django.shortcuts import render, HttpResponse, redirect
from . visitControl import getVisits, createVisit
from Patient.patientsControl import getPatientById, getPatients, getUserById
import json

# Display all visit data
def visitList(request):
    visitData = []
    visitInfos = getVisits()
    if visitInfos is not None:
        for visit in visitInfos:
            patientId = visit['patientId']
            patientInfo = getPatientById(int(patientId))
            date = visit['date']
            patientName = patientInfo['patientName']
            patientEmail = patientInfo['email']
            patientNumber = patientInfo['phone']
            userId = patientInfo['userId']
            userInfo = getUserById(int(userId))
            loginName = userInfo['loginName']
            time = visit['time']
            testName = visit['testName']
            visitId = visit['visitId']
            print("visit keys", visit.keys())
            if 'url' in visit.keys():
                url = visit['url']
            else:
                url = ""

            visitInfo = {
                'visitId': visitId,
                'patientName': patientName,
                'patientEmail': patientEmail,
                'date': date,
                'time': time,
                'testName': testName,
                'patientNumber': patientNumber,
                'url': url,
                'loginName': loginName
            }
            visitData.append(visitInfo)
        return render(request, "Visits/visitsList.html", {'visitData': visitData})
    else:
        return render(request, "Visits/visitsList.html")

# Add a new visit for selected patient
def addVisit(request):

    patientData = []
    patientInfos = getPatients()

    for patientInfo in patientInfos:
        patientName = patientInfo['patientName']
        patientId = patientInfo['patientId']
        patientNumber = patientInfo['phone']

        patientInfo = {
                'patientId': patientId,
                'patientName': patientName,
                'patientNumber': patientNumber
        }
        patientData.append(patientInfo)
    return render(request, "Visits/addVisit.html", {"patientData": patientData})

# Load email of a selected patient
def loadPatientEmail(request):

    patientId = request.GET.get('patientId')
    patientInfo = getPatientById(int(patientId))
    patientEmail = patientInfo['email']

    patientInfo = {
            'patientEmail': patientEmail,
            'patientId': patientId
    }
    return HttpResponse(json.dumps(patientInfo))

# Add created visit to Database
def addVisitToDB(request):
    print("request", request)
    visitInfos = getVisits()
    print("visitInfos",visitInfos)
    if visitInfos is None:
        lastvisitId = 0
    else:
        lastvisitId = visitInfos[0]['visitId']
        print("lastvisitId",lastvisitId)
    if request.method == "POST":
        visitId = int(lastvisitId) + 1
        testName = request.POST.get('testName')
        date = request.POST.get('date')
        time = request.POST.get('time')
        patientId = request.POST.get('patientId')
        print("patientId",patientId)



        visitInfo = {
            "visitId": int(visitId),
            "testName": testName,
            "date": date,
            "time": time,
            "patientId": int(patientId),
        }

        createVisit(visitInfo)
        return redirect('visitList')
    else:
        return redirect('visitList')
