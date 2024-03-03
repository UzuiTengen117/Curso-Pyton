texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print(" CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count((letras[0]))
cantidad_letras2 = texto.count((letras[1]))
cantidad_letras3 = texto.count((letras[2]))

print(f" Hemos  encontrado la letra ' {letras[0]} ' repetida {cantidad_letras1} veces")
print(f" Hemos  encontrado la letra ' {letras[1]} ' repetida {cantidad_letras2} veces")
print(f" Hemos  encontrado la letra ' {letras[2]} ' repetida {cantidad_letras3} veces")

print("\n")
print(" CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print(" letras de inicio y de fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La  leta inicial es '{letra_inicio}' la letra final es '{letra_final}'")

print("\n")
print(" TEXTO INVERTIDO")
palabras.reverse()
Texto_invertido = '  '.join(palabras)
print(f"Si ordenamos tu texto aleves va a decir: '{Texto_invertido}' ")

print("\n")
print(" BUSCANDO LA PALABRA PYTON")
Buscar_pyton = 'pyton' in texto
dic = {True: "Si", False: "No"}
print(f"La palabra ' Pyton ' {dic[Buscar_pyton]} se encuentra  en ele texto")
