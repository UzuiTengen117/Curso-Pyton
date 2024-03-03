Nombres = ['Juan Carlos', 'Jorgue Enrique','Emmanuel chaparro']
Edades = [65,29,42]
ciudades =['Mexico','Japon','Rusia']

conbinados = list(zip(Nombres,Edades,ciudades))

for Nombres,Edades,ciudades in conbinados:
    print(f"{Nombres} tiene {Edades} años y vive en {ciudades}")

