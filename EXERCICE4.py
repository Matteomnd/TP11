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
        heure = (self.__heure * 3600 +d1.__heure* 3600)/3600
        minutes = (self.__minute*60 + d1.__minute * 60)/60
        secondes = self.__seconde + d1.__seconde

        if minutes > 60 :
           minutes = minutes *1/60
           heure = int(minutes)
           minutes = minutes - heure
           minutes = minutes*60

        if seconde > 60 :

        return Duree(heure,minutes,secondes)



if __name__=='__main__':
    d1 = Duree(1,50,58)
    d2 = Duree(1,50,30)
    d3 = d1 + d2
    print(d3)
