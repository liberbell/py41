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
    def __init__(self, model="Model S", enable_auto_run=False):
        # self.model = model
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
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