## Animals_2a3.py -- a complete OO zoo !!               DMQ 6/10/04
'''
# Animal     -->    Reptile
# -------           -------
# Animal     -->    Mammal     -->    Bovine
# -------           -------           -------
# Animal     -->    Mammal     -->    Canine
# -------           -------           ------
# Animal     -->    Mammal     -->    Feline     -->    Cat
# -------           -------           -------           -------
# _numAnimals       _numMammals       _numFelines       _numCats
# home                                genus
# __init__()        __init__()        __init__()        __init__()
#                       .sound                              .sound
#                                                           .name
# show()            show()            show()            show()
#                   talk()                              talk()
#
'''
class Animal():
    home = "Tierra"
    _numAnimals = 0
    def __init__(self):
        Animal._numAnimals =     Animal._numAnimals + 1

    def show(self):
        print "Inventario:"
        print "Animales: %i"%Animal._numAnimals

class reptil(Animal):
    pass

class mammal(Animal):
    _numMammals = 0
    def __init__(self, s = "sonido"):
        mammal._numMammals +=1
        self.sound = s

    def show(self):
        Animal.show()
        print "Mamiferos: %i"%mammal._numMammals

    def talk(self):
        print "Sonido:  " + self.sound

class bobino(mammal):
    pass

class canino(mammal):
    pass

class felino(mammal):
    _numfelinos = 0
    def __init__(self):
        felino._numfelinos += 1
        self.sound = "sonido felino"
    def show(self):
        Mammal.show()
        print "Numero de felinos %i"%felino._numfelinos

class gato(felino):
    _numcat = 0

    def __init__(self,s = "miau"):
        Animal.__init__(self)
        gato._numcat += 1
        self.sound = s

    def show(self):
        felino.show()
        print "Gatos %d"%gato._numcat

if __name__ == '__main__':
    a = Animal()
    m = mammal()
    gatos =gato()
    deslizante = reptil()
    beee = bobino()
    gatete1 = gatos
    a.show()
    gatete1.talk()
    m.talk()
