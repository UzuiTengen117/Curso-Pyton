def contar_primos(numero):

    primos= [2]
    interaciones =3

    if numero <2:
        return 0

    while interaciones<= numero:
        for n in range(3,interaciones,2):
            if interaciones % n ==0:
                interaciones +=2
                break
        else:
            primos.append(interaciones)
            interaciones +=2
    print(primos)
    return  len(primos)

print(contar_primos(300))

















"""----------------------------------------------------------------------------"""
"""def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador +1 == len(args):
            return False

        elif args[contador]==0 and args[contador+1]==0:
            return True
        else:
            contador +=1
    return False

print(ceros_vecinos(0,3,5,6,7,5,2,42,32,1,4,21,4,32,1,23,0,2,4,234,32,14,0))"""














"""---------------------------------------------------------------------------"""
"""def letras_unicas(palabra):

    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista



print(letras_unicas("ETRETENIDO"))"""







""""-----------------------------------------------------------------------------------------------------"""
"""def devolver_distintos(a,b,c):

        suma=a+b+c
        lista =[a,b,c]

        if suma > 15:
            return max(lista)
        elif suma < 10 :
            return min (lista)
        else:
            lista.sort()
            return  lista[1]


print(devolver_distintos(7,2,4))
"""