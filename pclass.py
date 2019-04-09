#!/usr/bin/python3
class MyClass:
    def __init__(self, name=None, lastname=None):
        self.name = name
        self.lastname = lastname

class KolaskiFamily(MyClass):
    def __init__(self, name):
        super().__init__(name, "Kolaski")

class FullData(MyClass):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname)
        self.age = age
