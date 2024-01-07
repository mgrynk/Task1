#from pprint import pprint
from people import Person
import yaml



qa = "QA"
devops= "DevOps"
with open('Pesons.yaml', 'r') as file:
    data = yaml.safe_load(file)
#    print(data['Person1'])
    Name = data['Person1']['Name']
    Surname = data['Person1']['Surname']
    Age = data['Person1']['Age']
    Sex = data['Person1']['Sex']
    prof = data['Person1']['Prof']
#    print(prof)

#print(data)
file.close()

p1 = Person(Name, Surname, Age, Sex, prof)
p1.myfunc()
"""
/
"""