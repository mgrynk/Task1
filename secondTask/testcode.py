import yaml

def list_of_Persons(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
        pers = list(data.items())[0][1] 
    return pers

def verification_of_profession(check_list):
    for x in check_list:
        if x['Person'].get('Prof') == "QA":
            print(x['Person'].get('Name') + " " + x['Person'].get('Surname') + " Good luck")
        elif x['Person'].get('Prof') == "PM" and x['Person'].get('Sex') == "FeMale":
            print(x['Person'].get('Name') + " " + x['Person'].get('Surname') + " Well done")
        elif x['Person'].get('Prof') == "PM" and x['Person'].get('Sex') == "Male":
            print(x['Person'].get('Name')+ " " + x['Person'].get('Surname') + " Not the best profesion for you")
        elif x['Person'].get('Prof') == "Dev":
            print(x['Person'].get('Name') + " " + x['Person'].get('Surname') + " Good")
        elif x['Person'].get('Prof') == "DevOps":
            print(x['Person'].get('Name') + " " + x['Person'].get('Surname') + " You are the best, rockstar!!")

def main():
    path = "Persons.yaml"
    pers = list_of_Persons(path)
    verification_of_profession(pers)


if __name__ == "__main__":
    main()