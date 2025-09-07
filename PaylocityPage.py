import requests
from bs4 import BeautifulSoup
import jsonData


def info():
    url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/Employees"
    session = requests.Session()
    infoRequuest = session.get(url,headers={"Authorization":"Basic VGVzdFVzZXI3OTc6VCR9bmVsREw4ayNR"})
    soup = BeautifulSoup(infoRequuest.content, 'html.parser')
    print(f"response: {soup} ")
    assert infoRequuest.status_code == 200

def addEmployee():
    url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/Employees"
    session = requests.Session()
    addRequuest = session.post(url, headers=jsonData.dataJson.employeeInformationHeaders(""),data=jsonData.dataJson.employeeInformation(""))
    assert addRequuest.status_code == 200
    EmployeeID = addRequuest.json().get("id")
    return EmployeeID

def updateEmployee(EmployeeID):
    url = f"https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/Employees"
    session = requests.Session()
    putRequuest = session.put(url, headers=jsonData.dataJson.employeeInformationHeaders(""),data=jsonData.dataJson.employeeinformationUpdate(EmployeeID))
    assert putRequuest.status_code == 200


def deleteEmployee(EmployeeID):
    url = f"https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/Employees/{EmployeeID}"
    session = requests.Session()
    DeleteRequuest = session.delete(url, headers=jsonData.dataJson.employeeInformationHeaders(""))
    assert DeleteRequuest.status_code == 200