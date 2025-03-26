import pygame
import sys
import math
import os

# Inicializar pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)

# Tamaño de la ventana
TAMAÑO_VENTANA = 300
ANCHO_CELDA = TAMAÑO_VENTANA // 3

# Crear la ventana
ventana = pygame.display.set_mode((TAMAÑO_VENTANA, TAMAÑO_VENTANA))
pygame.display.set_caption("Ta-Te-Ti con IA y Poda Alfa-Beta")

files=["tablero.png", "cruz.png", "circulo.png"]

imagenes={}

for file in files:
    # Obtiene la ruta absoluta del directorio actual del script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta completa de la imagen de manera dinámica
    ruta_imagen = os.path.join(directorio_actual, "IMG", file)

    # Carga la imagen y la almacena en el diccionario
    imagenes[file] = pygame.image.load(ruta_imagen)

# Redimensionar las imágenes para que encajen en la ventana y las celdas
imagen_tablero = pygame.transform.scale(imagenes["tablero.png"], (TAMAÑO_VENTANA, TAMAÑO_VENTANA))
imagen_cruz = pygame.transform.scale(imagenes["cruz.png"], (ANCHO_CELDA, ANCHO_CELDA))
imagen_circulo = pygame.transform.scale(imagenes["circulo.png"], (ANCHO_CELDA, ANCHO_CELDA))

# Definir el tablero inicial
tablero = [' ' for _ in range(9)]

def dibujar_tablero():
    ventana.blit(imagen_tablero, (0, 0))
    for i in range(9):
        fila = i // 3
        columna = i % 3
        x = columna * ANCHO_CELDA
        y = fila * ANCHO_CELDA
        
        if tablero[i] == 'X':
            ventana.blit(imagen_cruz, (x, y))
        elif tablero[i] == 'O':
            ventana.blit(imagen_circulo, (x, y))

def hay_ganador(tabla, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacion in combinaciones_ganadoras:
        if tabla[combinacion[0]] == tabla[combinacion[1]] == tabla[combinacion[2]] == jugador:
            return True
    return False

def tablero_lleno(tabla):
    return ' ' not in tabla

def evaluar(tabla):
    if hay_ganador(tabla, 'O'):
        return 1
    elif hay_ganador(tabla, 'X'):
        return -1
    else:
        return 0

# Nuevo algoritmo Minimax con poda alfa-beta
def minimax_alfabeta(tabla, profundidad, alfa, beta, esMaximizingPlayer):
    if hay_ganador(tabla, 'O') or hay_ganador(tabla, 'X') or tablero_lleno(tabla):
        return evaluar(tabla)
    
    if esMaximizingPlayer:
        mejor_valor = -math.inf
        for i in range(9):
            if tabla[i] == ' ':
                tabla[i] = 'O'
                valor = minimax_alfabeta(tabla, profundidad + 1, alfa, beta, False)
                tabla[i] = ' '
                mejor_valor = max(mejor_valor, valor)
                alfa = max(alfa, mejor_valor)
                if beta <= alfa:
                    break  # Poda beta
        return mejor_valor
    else:
        mejor_valor = math.inf
        for i in range(9):
            if tabla[i] == ' ':
                tabla[i] = 'X'
                valor = minimax_alfabeta(tabla, profundidad + 1, alfa, beta, True)
                tabla[i] = ' '
                mejor_valor = min(mejor_valor, valor)
                beta = min(beta, mejor_valor)
                if beta <= alfa:
                    break  # Poda alfa
        return mejor_valor

# Función actualizada para la IA que utiliza Minimax con poda alfa-beta
def mejor_movimiento_ia(tabla):
    mejor_valor = -math.inf
    mejor_movimiento = None
    alfa = -math.inf
    beta = math.inf
    
    for i in range(9):
        if tabla[i] == ' ':
            tabla[i] = 'O'
            valor = minimax_alfabeta(tabla, 0, alfa, beta, False)
            tabla[i] = ' '
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = i
            alfa = max(alfa, mejor_valor)
    return mejor_movimiento

def manejar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            fila = y // ANCHO_CELDA
            columna = x // ANCHO_CELDA
            indice = fila * 3 + columna
            
            if tablero[indice] == ' ':
                tablero[indice] = 'X'
                if hay_ganador(tablero, 'X'):
                    print("¡Felicidades! ¡Has ganado!")
                    pygame.quit()
                    sys.exit()
                elif tablero_lleno(tablero):
                    print("¡Es un empate!")
                    pygame.quit()
                    sys.exit()
                else:
                    movimiento_ia = mejor_movimiento_ia(tablero)
                    tablero[movimiento_ia] = 'O'
                    if hay_ganador(tablero, 'O'):
                        print("¡La IA ha ganado!")
                        pygame.quit()
                        sys.exit()

# Bucle principal del juego
while True:
    manejar_eventos()
    dibujar_tablero()
    pygame.display.update()