class Matrix :
    def __init__(self,data):
        self.__data = data

    def __add__(self,m1):
        return Matrix(self.__data + m1.__data)

    def __sub__(self,m1):
        return Matrix(self.__data - m1.__data)
    
    def
