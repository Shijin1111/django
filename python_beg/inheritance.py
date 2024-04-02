class Animal:
    def __init__(self):
        print("animal created")
    def printing(self):
        print("animal")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("dog is created")
    def __str__(self):
        return "hello"
dog=Dog()
dog.printing()
print(dog)
