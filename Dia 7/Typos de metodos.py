class Pajaro:
  
  alas =True

  def __init__ (self,color,especie):
    self.color=color
    self.especie=especie
   
  def piar(self):
    print('Pio ')


  def Volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')  
        self.piar()
  
  def pintar_negro(self):
        self.color='Negro'
        print(f'Ahora el pagaro es de color {self.color}')  

  
  @classmethod
  def poner_huevos(cls,cantidad):
      print(f'puso {cantidad} huevos')
      cls.alas=False
      print(Pajaro.alas)


  @staticmethod
  def mirar():
      print("El pajaro mira")

Pajaro.mirar()

