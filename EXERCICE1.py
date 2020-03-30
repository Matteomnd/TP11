class Cercle :
    def __init__(self,rayon):
        self.__rayon= rayon

    def get_rayon(self):
        return self.__rayon

    def __add__(self,c1):
        return Cercle(self.__rayon + c1.__rayon)

    def __lt__(self,c1):
        return self.__rayon < c1.__rayon

    def __gt__(self,c1):
        return self.__rayon > c1.__rayon


    def __str__(self):
        return "taille du rayon :"+ str(self.__rayon)




if __name__ == '__main__':
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    print(isinstance(c3,Cercle))
    c4 = c1 < c2
    print(isinstance(c4,Cercle))
    c5 = c2 > c3
    print(isinstance(c5, Cercle))
    print(c3)
