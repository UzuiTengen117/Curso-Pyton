class Pajaro:
  
  alas =True

  def __init__ (self,color,especie):
    self.color=color
    self.especie=especie
   
  def piar(self):
    print('Pio mi color es {}'.format(self.color))


  def Volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')  
    


piolin=Pajaro('amarillo','canario')
piolin.piar()