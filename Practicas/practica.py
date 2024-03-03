import  turtle

ventana= turtle.Screen()
ventana.bgcolor("black")
tortuga= turtle.Turtle()
tortuga.speed(50000)
tortuga.color('Gold')
numero_estrella=100


for i in range(numero_estrella*100):
    tortuga.forward(i*1)
    tortuga.right(238)

ventana.exitonclick()
ventana.close()
