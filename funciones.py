import turtle
import random
import time

# =====================================================
#  CAJA DE HERRAMIENTAS (funciones de regalo)
#  Estas ya vienen hechas: solo las usamos.
# =====================================================

def nueva_pantalla(ancho, alto, color_fondo, titulo):
    pantalla = turtle.Screen()
    pantalla.setup(ancho, alto)
    pantalla.bgcolor(color_fondo)
    pantalla.title(titulo)
    pantalla.screensize(ancho - 10, alto - 10)   # para que en Mac quede centrada
    pantalla.tracer(0)
    return pantalla


def nuevo_lapiz():
    lapiz = turtle.Turtle()
    lapiz.hideturtle()
    lapiz.penup()
    return lapiz


def dibujar_pista(salida, meta):
    lapiz = nuevo_lapiz()
    # El pasto de la pista
    lapiz.goto(salida - 30, -210)
    lapiz.color("#EAF7EF")
    lapiz.begin_fill()
    for i in range(2):
        lapiz.forward(meta - salida + 60)
        lapiz.left(90)
        lapiz.forward(420)
        lapiz.left(90)
    lapiz.end_fill()
    # Las líneas de salida y meta: lunares de colores
    for x in [salida, meta]:
        for i in range(21):
            if i % 2 == 0:
                color = "#C39BD3"
            else:
                color = "#F5B7D0"
            lapiz.goto(x, -200 + i * 20)
            lapiz.dot(14, color)
    # Los letreros
    lapiz.color("#8E44AD")
    lapiz.goto(salida, -240)
    lapiz.write("SALIDA", align="center", font=("Arial", 14, "bold"))
    lapiz.goto(meta, -240)
    lapiz.write("META 🏁", align="center", font=("Arial", 14, "bold"))


def escribir(texto, x, y, color, tamano):
    lapiz = nuevo_lapiz()
    lapiz.goto(x, y)
    lapiz.color(color)
    lapiz.write(texto, align="center", font=("Arial", tamano, "bold"))
    return lapiz


def cuenta_regresiva(pantalla):
    for numero in ["3", "2", "1", "¡YA! 🚀"]:
        lapiz = escribir(numero, 0, -20, "#E91E8C", 60)
        pantalla.update()
        time.sleep(0.8)
        lapiz.clear()
    pantalla.update()


def desactivar_teclas(pantalla):
    for tecla in ["Right", "space", "Up", "Down"]:
        pantalla.onkey(None, tecla)


enter_presionado = False


def presionar_enter():
    global enter_presionado
    enter_presionado = True


def esperar_enter(pantalla):
    global enter_presionado
    escribir("Presiona ENTER para jugar otra vez", 0, -90, "#5D6D7E", 16)
    enter_presionado = False
    pantalla.onkey(presionar_enter, "Return")
    pantalla.listen()
    while not enter_presionado:
        pantalla.update()
        time.sleep(0.05)


# =====================================================
#  FUNCIONES QUE ESCRIBIMOS NOSOTRAS
# =====================================================

# =====================================================
#  FUNCIONES QUE ESCRIBIMOS NOSOTRAS
# =====================================================
# Clase 1: escribe aquí nueva_tortuga(color, x, y) y activar_teclas(pantalla, jugadora, carriles)
