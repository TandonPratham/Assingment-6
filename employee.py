import json

    
# with open(r'C:\Users\ASUS\Desktop\Assigment\Assigment\_6_Assingment_6.py\_1_\employee.json','r') as file:
#     data = json.load(file)
#     print(data)

class Employees:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open('employee.json','r') as f :
    data = json.load(f)

employees = [Employees(e['Name'], e['DOB'], e['Height'], e['City'] , e['State']) for e in data['Employees']]

for employee in employees:
    print(employee.name, employee.dob, employee.height, employee.city, employee.state)