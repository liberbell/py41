class Person(object):
    def talk(self):
        print("talk")

class Car(object):
    def run(self):
        print("run")

class PersonCarRobot(Person, Car):
    def fly(self):
        print("fly")