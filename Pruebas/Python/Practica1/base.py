class Student:
    def __init__(self, name, lastname, age):
        self.__name=name
        self.__lastname=lastname
        self.__age=age

    #get method
    def getName(self):
        return self.__name
    def getLastname(self):
        return self.__lastname
    def getAge(self):
        return self.__age
    
    #set method
    def setName(self, name):
        self.__name=name
    def setLastname(self, lastname):
        self.__lastname=lastname
    def setAge(self, age):
        self.__age=age