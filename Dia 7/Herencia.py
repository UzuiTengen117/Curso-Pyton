class padere:
    def hablar(self):
        print("Hola")



class hijo(padere):
    pass


class nieto(hijo):
    pass

mi_nieto =nieto()
mi_nieto.hablar()

