from django.shortcuts import render, redirect
from Patient.patientsControl import getPatientById
from Visits.visitControl import getVisits, getVisitById
from .reportControl import getReports, createReport, reportUploadTODB, getReportById
import json
from django.http import HttpResponse, StreamingHttpResponse
import urllib.request


# It Will display reportsList
def reportsList(request):
    reportData = []
    reportInfos = getReports()
    if reportInfos is not None:
        for report in reportInfos:
            patientId = report['patientId']
            patientInfo = getPatientById(int(patientId))
            reportName = report['reportName']
            patientName = patientInfo['patientName']
            patientNumber = patientInfo['phone']
            patientEmail = patientInfo['email']
            reportDate = report['creationDate']
            visitId = report['visitId']
            reportId = report['reportId']

            reportInfo = {
                'patientName': patientName,
                'patientEmail': patientEmail,
                'reportName': reportName,
                'reportDate': reportDate,
                'visitId': visitId,
                'patientNumber': patientNumber,
                'reportId': reportId
            }
            reportData.append(reportInfo)
        return render(request, "Report/reportsList.html", {'reportData': reportData})
    else:
        return render(request, "Report/reportsList.html")


# It return the patientName & visitId
def addReport(request):
    visitData = []
    try:
        visitInfos = getVisits()
        for visitInfo in visitInfos:
            visitId = visitInfo['visitId']
            patientId = visitInfo['patientId']
            patientInfo = getPatientById(int(patientId))
            patientName = patientInfo['patientName']
            visit = {
                'visitId': visitId,
                'patientName': patientName
            }
            visitData.append(visit)
        return render(request, "Report/addReport.html", {"visitData": visitData})
    except:
        message = "Something went wrong, please try again"
        return render(request, "home.html", {"msg": message})


# Click On VisitID it will load patientData
def loadPatientData(request):
    try:
        visitId = request.GET.get('visitId')
        visitInfo = getVisitById(int(visitId))
        patientId = visitInfo['patientId']
        patientInfo = getPatientById(int(patientId))
        patientName = patientInfo['patientName']
        patientNumber = patientInfo['phone']
        creationDate = visitInfo['date']
        testName = visitInfo['testName']

        if 'url' in visitInfo.keys():
            url = visitInfo['url']
        else:
            url = ""
        patientData = {
            'patientName': patientName,
            'patientNumber': patientNumber,
            'patientId': patientId,
            'creationDate': creationDate,
            'testName': testName,
            'url' : url
        }
        return HttpResponse(json.dumps(patientData))
    except:
        message = "Something went wrong, please try again"
        return render(request, "home.html", {"msg": message})


# addReportToDB return the reportInfo
def addReportToDB(request):
    reportInfos = getReports()
    if reportInfos is None:
        lastReportId = 1
    else:
        lastReportId = reportInfos[0]['reportId']
    if request.method == "POST":
        reportId = int(lastReportId) + 1
        visitId = request.POST.get('selectVisitId')
        patientId = request.POST.get('patientId')
        print("patientId", patientId)
        creationDate = request.POST.get('creationDate')
        reportName = request.POST.get('reportName')
        print("request", request)
        print("FILE:", request.FILES)
        url = reportUploadTODB(request.FILES, patientId, reportId)

        reportInfo = {
            'reportId': int(reportId),
            'visitId': int(visitId),
            'patientId': int(patientId),
            'reportName': reportName,
            'creationDate': creationDate,
            'url': url,
        }

        createReport(reportInfo)
        return redirect('reportsList')
    else:
        return redirect('reportsList')

# It will display report on clicking on report name by particular report id
def displayreport(request, reportId):
    reportInfo = getReportById(int(reportId))
    url = reportInfo['url']
    url = url
    response = StreamingHttpResponse(stream_pdf(url), content_type="application/pdf")
    return response

def stream_pdf(url, chunk_size=8192):
    sock = urllib.request.urlopen(url)
    while True:
        content = sock.read(chunk_size)
        if not content: break
        yield content
