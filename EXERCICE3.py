class Rational :
    def __init__(self, numerator, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def __add__(self, f1):
        if isinstance(f1, Rational):
            if self.__denominator==0 or f1.__denominator==0 :
                return 'erreur : division par 0'
            return Rational(int(self.__numerator*f1.__denominator + self.__denominator*f1.__numerator)/int(self.__denominator*f1.__denominator))
        else :
            print('no instance of f1')

    def __sub__(self,f1):
        if isinstance(f1, Rational):
             if self.__denominator==0 or f1.__denominator==0 :
                 return 'erreur : division par 0'
             return Rational((self.__numerator*f1.__denominator - self.__denominator*f1.__numerator)/(self.__denominator*f1.__denominator))

        else :
            print('no instance of f1')



    def __eq__(self,f1):
        if isinstance(f1, Rational):
            if self.__denominator==0 or f1.__denominator==0:
                return self.__numerator, f1.__numerator
            else :
                reste1 = self.__numerator % self.__denominator
                reste2 = f1.__numerator % f1.__denominator


            return (self.__numerator / reste1)==(f1.__numerator/reste2), (self.__denominator/reste1)==(f1.__denominator/reste2)

    def __str__(self):
        return 'fraction 1 :'+str(self.__numerator)+'/'+str(self.__denominator)



if __name__ == '__main__' :
    f1 = Rational(3,2)
    f2 = Rational(1,2)
    f3 = f1 + f2
    f4= f1 -f2
    f5 = f1 == f2
    print(f3)
    print (f4)
    print (f5)



