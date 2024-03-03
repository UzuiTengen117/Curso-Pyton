class Vaca:


    def __init__(self,Nombre) :
        self.Nombre = Nombre

    def hablar(self):
        print(self.Nombre+"Dice Muu")

class Obeja:

    def __init__(self,Nombre) :
        self.Nombre = Nombre

    def hablar(self):
        print(self.Nombre+"Dice Bee")

Vaca1 =  Vaca('Aurora')
Obeja1= Obeja('Nube')



def animal_Habla(animal):
    animal.hablar()

animal_Habla(Obeja1)