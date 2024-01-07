class Person:
  def __init__(self, name, surname, age, sex, prof):
    self.name = name
    self.surname= surname
    self.age = age
    self.sex = sex
    self.proffestion = prof

  def myfunc(self):
      if self.proffestion == "QA":
        print(self.name + self.surname + " Please chane your profesion")
      elif self.proffestion == "PM" and self.sex == "Female":
        print(self.name + self.surname + " Well done")
      elif self.proffestion == "PM" and self.sex == "Male":
        print(self.name + self.surname + " Not the best profesion for you")
      elif self.proffestion == "Dev":
        print(self.name + self.surname + " Good")
      elif self.proffestion == "DevOps":
        print(self.name + self.surname + "You are the best, rockstar!!")

"""
p1 = Person("John ", "Test", 36, "Male", "PM")
p2 = Person("Maks ", "Tester", 22, "Male", "QA")
p3 = Person("Toha ", "Petrovich ", 21, "Male", "DevOps")
p1.myfunc()
p2.myfunc()
p3.myfunc()
"""