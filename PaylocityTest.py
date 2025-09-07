import pytest

from PaylocityPage import *

def test_info():
    info()

def test_Employee():
    employeeID = addEmployee()
    updateEmployee(employeeID)
    deleteEmployee(employeeID)
