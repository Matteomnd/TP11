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
        return np.rank(self.__data)<np.rank(m1.__data)

    def __gt__(self, m1):
        return np.rank(self.__data)>np.rank(m1.__data)

    def __str__(self):
        return str(self.__data)


matrix_1= np.array([[2,5],[6,7]])
matrix_2 = np.array([[4,7],[6,2]])
m1= matrix_1 + matrix_2
print(m1)
m2 = matrix_1 - matrix_2
print(m2)
m3 = matrix_1 * matrix_2
print(matrix_1+=matrix_2)
m6 = m1 > m2
