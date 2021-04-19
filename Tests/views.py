from django.shortcuts import render
from . testControl import getTests, createTest, updateTest, deleteTest

# It Will Display testsList  
def testsList(request):
    testInfos = getTests()
    return render(request, "Tests/testslist.html", {'testInfos': testInfos})

# 
def addTest(request):
    return render(request, "Tests/addTest.html")

# addTestToDB return testInfo to createTest
def addTestToDB(request):
    testInfos = getTests()
    lastTestId = testInfos[0]['testId']
    if request.method == "POST":
        testId = int(lastTestId) + 1
        testName = request.POST.get('testName')
        price = request.POST.get('price')

        testInfo = {
            "testId": int(testId),
            "testName": testName,
            "price": int(price)
        }
        createTest(testInfo)
        testInfos = getTests()
        return render(request, "Tests/testslist.html", {'testInfos': testInfos})
    else:
        return render(request, "Tests/testslist.html", {'testInfos': testInfos})

# Clicking On Edit Btn it will print Old Value depends on testId 
def editTest(request, testName, price, testId):
    price = price
    testinfo = {
        "testId": testId,
        "testName": testName,
        "price": int(price)
    }
    return render(request, "Tests/editTest.html",  {"testinfo":testinfo})

# Update Test 
def updateTestToDB(request, testId):
    if request.method == "POST":
        testName = request.POST.get('testName')
        price = request.POST.get('price')

        test = {
            "testName": testName,
            "price": int(price)
        }
        updateTest(test, testId)
        testInfos = getTests()
        return render(request, "Tests/testslist.html",  {"testInfos": testInfos})
    else:
        return render(request, "Tests/testslist.html")

# On clicking on delete button it will print all ol values
def deletetest(request, testName, price, testId):
    price = price
    testinfo = {
        "testId": testId,
        "testName": testName,
        "price": int(price)
    }
    return render(request, "Tests/deleteTest.html",  {"testinfo":testinfo})

# Clicking on delete button it will delete particular entry from db
def deleteTestFromDB(request, testId):
    if request.method == "POST":
        testName = request.POST.get('testName')
        price = request.POST.get('price')

        test = {
            "testName": testName,
            "price": int(price)
        }
        deleteTest(test,testId)
        testInfos = getTests()
        return render(request,"Tests/testslist.html",{"testInfos":testInfos})
    else:
        return render(request, "Tests/testslist.html")