class CD:

    def __init__(self,autor,titulo,canciones):
        self.auotor= autor
        self.titulo= titulo
        self.canciones= canciones

    def __str__(self) :
        return f"Albun: {self.titulo} de {self.auotor}"
        
    def __len__(self):
        return self.canciones

    def __del__ (self):
        print("Se ha eliminado el cd")

mi_cd=CD('Pinck floid','the wall',24)

