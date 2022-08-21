s = "fkipqxjikrjlkjsfckcdf"

# print(s.capitalize())

class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print("I am {}, hello.".format(self.name))
        self.run(10)

    def run(self, num):
        print("run" * num)

    def __del__(self):
        print("good bye")


# person = Person("mike")
# person.say_something()

# del person

# print("#########")

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print("run")

class ToyotaCar(Car):
    def run(self):
        print("fast")

class TeslaCar(Car):
    def __init__(self, model="Model S", enable_auto_run=False, passwd="1234"):
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == "456":
            self._enable_auto_run = is_enable
        else:
            raise ValueError
        

    def auto_run(self):
        print("super fast")

# car = Car()
# car.run()

# print("#####")
# toyota_car = ToyotaCar("Lexus")
# print(toyota_car.model)
# toyota_car.run()

# tesla_car = TeslaCar("Model S")
# print(tesla_car.model)
# tesla_car.run()
# tesla_car.auto_run()

tesla_car = TeslaCar("Model S")
print(tesla_car.enable_auto_run)

tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)