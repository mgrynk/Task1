from people import Person
import yaml


def pars_persons(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
        print(data)
        person = Person(data['Person1']['Name'],
                        data['Person1']['Surname'],
                        data['Person1']['Age'],
                        data['Person1']['Sex'],
                        data['Person1']['Prof']
                        )
        file.close()
    return person


def verification_of_profession(check_person):
    if check_person.profesion == "QA":
        print(check_person.name + " " + check_person.surname + " Please chane your profesion")
    elif check_person.profesion == "PM" and check_person.sex == "Female":
        print(check_person.name + " " + check_person.surname + " Well done")
    elif check_person.profesion == "PM" and check_person.sex == "Male":
        print(check_person.name + " " + check_person.surname + " Not the best profesion for you")
    elif check_person.profesion == "Dev":
        print(check_person.name + " " + check_person.surname + " Good")
    elif check_person.profesion == "DevOps":
        print(check_person.name + " " + check_person.surname + "You are the best, rockstar!!")


def main():
    path = "pers.yaml"
    person = pars_persons(path)
    verification_of_profession(person)


if __name__ == "__main__":
    main()

"""
/
"""
