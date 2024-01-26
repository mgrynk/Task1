import yaml
import logging
from peoples import People

logging.basicConfig(level=logging.INFO,filename="yml_log.log",filemode="w")

def list_of_Persons(path):
    logging.info('Open YAML File')
    with open(path, 'r') as f:
        logging.info('Create object(dict) with data from Yaml file')
        data = yaml.safe_load(f)
        logging.info('Creale object with persons from  data object')
        pers = People(data)
    logging.info('Create list of persons')
    persons_list = list(pers.Persons)
    return persons_list

def verification_of_profession(check_list):
    logging.info("Prof verification")
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