from dataclasses import dataclass

# 12
# @dataclass
# class Product():
#     __name: str
#     __store_name: str
#     __price: int
#
# @dataclass
# class Store():
#    def  __init__(self):

# 2
import math
class RightTriangle():
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__z=(self.__x**2+self.__y**2)**(1/2)
    def change_side(self,side,percent):
        """x and y are leg of right triangle"""
        if side=='x':
            self.__x*=(100+percent)/100
        elif side=='y':
            self.__y*=(100+percent)/100
        else:
            print('введены не правильные значения')

    def get_sides(self):
        return (self.__x,self.__y,self.__z)
    def radius(self):
        return self.__z/2

    def perimetr(self):
        return self.__z+self.__x+self.__y
    def angles(self):
        angles_dict={}
        angles_dict['xy']=90
        angles_dict['yz']=math.degrees(math.acos((self.__x**2+self.__z**2-self.__y**2)/(2*self.__x*self.__z)))
        angles_dict['zx']=90-angles_dict['yz']
        return angles_dict

tr1=RightTriangle(3,4)
print(tr1.get_sides())
print(tr1.radius())
print(tr1.perimetr())
print(tr1.angles())
tr1.change_side('y',200)
print(tr1.get_sides())

# 3
class TAray():
    def __init__(self, values=None, num=None):
        self.__values=values


    def __copy__(self):

