def prueba (num1,num2,*args,**kwargs):

    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")


    for args in args:
        print(f"args = {args}")

    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")



args =[72,826,3871,23,]
kwargs ={'x':'uno','y':'dos','z':'tres'}

prueba(15,63,*args,**kwargs)








"""def suma (**kwargs):

    total =0
    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")
        total+=valor

    return total

print(suma(x=3, y=5,z=2))"""