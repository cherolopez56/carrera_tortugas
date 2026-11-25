import random
import time
import turtle

import funciones as f

# ---------- Configuración de la carrera ----------
SALIDA = -260                     # x de la línea de salida
META = 260                        # x de la línea de meta
CARRILES = [150, 50, -50, -150]   # y de cada carril (de arriba a abajo)

pantalla = f.nueva_pantalla(700, 560, "#FFF0F7", "Carrera de Tortugas")


# Escribe aquí tu función jugar() siguiendo el pseudocódigo de la guía.
# Al final del archivo no olvides llamarla:  jugar()
