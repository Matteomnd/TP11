import numpy as np
class Matrix :
    def __init__(self,data):
        self.__data = data

    def __add__(self,m1):
        return Matrix(self.__data + m1.__data)

    def __sub__(self,m1):
        return Matrix(self.__data - m1.__data)
    
    def __iadd__(self,m1):
        self.__data += m1.__data

    def __isub__(self,m1):
        self.__data -= m1.__data

    def __imul__(self, m1):
        self.__data *= m1.__data

    def __mul__(self, m1):
        return Matrix(np.dot(self.__data , m1.__data)

    def __lt__(self,m1):

