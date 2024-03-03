nombre = input("Por favor, dime tu nombre: ")
ventas= int( input("Digita tus ventas totales del mes: "))

Commission = round(ventas * 13 / 100, 2)
print(f"Hola {nombre}, Tus comisiones de este mes son de ${Commission}")

