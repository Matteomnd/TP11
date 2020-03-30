class Duree :
    def __init__(self,heure, minute, seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde =seconde

    def get_heure(self):
        return self.__heure

    def get_minute(self):
        return self.__minute

    def get_seconde(self):
        return self.__seconde

    def __str__(self):
        return 'Durée :'+str(self.__heure)+'h'+str(self.__minute)+'m'+str(self.__seconde)+'s'

    def __add__(self,d1):
        secondes = self.__seconde + d1.__seconde
        minutes = (self.__minute + d1.__minute ) + secondes//60
        heure = (self.__heure + d1.__heure) + minutes //60

        return Duree(heure,minutes%60,secondes%60)



if __name__=='__main__':
    d1 = Duree(1,50,58)
    d2 = Duree(1,50,30)
    d3 = d1 + d2
    print(d3)
