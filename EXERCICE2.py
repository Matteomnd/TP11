class Complex :
    def __init__(self, real, imaginar):
        self.__real =real
        self.__imaginar = imaginar

    def get_Real(self):
        return self.__real

    def get_Imaginar(self):
        return self.__imaginar

    def __add__(self,z1):
        return Complex(self.__real + z1.__real,self.__imaginar + z1.__imaginar)

    def __sub__(self, z1):
        return Complex(self.__real - z1.__real,self.__imaginar - z1.__imaginar)

    def __mul__(self, z1):
        return Complex(self.__real*z1.__real +self.__imaginar*z1.__imaginar, self.__real*z1.__imaginar +self.__imaginar*z1.__real)

    def __div__(self):

    def __abs__(self):
        return Complex()

    def __eq__(self,z1):
        return self.__real == z1.__real and self.__imaginar == z1.__imaginar

    def __ne__(self, z1):
        return self.__real != 
