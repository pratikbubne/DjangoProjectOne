from django.shortcuts import render, redirect
from .patientsControl import getPatients, updatePatient

# It will Display Patient List & Render to HTML
def patientsList(request):
    patientInfos = getPatients()
    patientData = []


    if patientInfos is not None:
        for patient in patientInfos:
            patientId = patient['patientId']
            patientName = patient['patientName']
            age = patient['age']
            gender = patient['gender']
            phone = patient['phone']
            email = patient['email']

            patientInfo = {

                'patientId': patientId,
                'patientName': patientName,
                'age': age,
                'gender': gender,
                'phone': phone,
                'email': email,
            }
            patientData.append(patientInfo)
        return render(request, "Patient/patientsList.html", {'patientData': patientData})
    else:
        return render(request, "Patient/patientsList.html")


def editPatient(request, patientName, age, gender, phone, patientId, email):

    patientinfo = {

        "patientName": patientName,
        "age": int(age),
        "gender": gender,
        "phone": int(phone),
        "patientId": patientId,
        "email": email
    }
    return render(request, "Patient/editPatient.html", {'patientinfo': patientinfo})

def updatePatientToDB(request, patientId):
    if request.method == "POST":
        patientName = request.POST.get('patientName')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        patient = {
            "patientName": patientName,
            "age": int(age),
            "gender": gender,
            "phone": int(phone),
            "email": email,

        }
        updatePatient(patient, patientId)
        return redirect(patientsList)
    else:
        return render(request, "Patient/patientslist.html")