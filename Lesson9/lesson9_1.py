class MyClass:
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

    @staticmethod
    def staticmethod():
        print('static method called')


class ChildClass(MyClass):
    TOTAL_OBJECTS=0
    pass


a= MyClass()
a.staticmethod()
MyClass.staticmethod()

my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()

MyClass.total_objects()
my_obj3.total_objects()

childobj=ChildClass()
ChildClass.total_objects()
childobj.staticmethod()
childobj.total_objects()