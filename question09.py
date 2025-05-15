# class Customer(Person) is setting up a child class of the Person class

# that code uses the "magic method" to set up a name attribute, probably
# in the Person class since there is no super() call first

class Person:
    def __init__(self, name):
        self.name = name

    def speak(self, words):
        print(str(words))

class Customer(Person):
    def __init__(self, name):
        super().__init__(name)


customer = Customer("Joey")
customer.speak(f"{customer.name} says hello")