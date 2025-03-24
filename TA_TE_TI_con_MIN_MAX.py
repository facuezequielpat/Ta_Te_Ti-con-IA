import pygame
import sys
import math

# Inicializar pygame
pygame.init()

# Definir colores (aunque ahora usaremos una imagen de tablero, por lo que no los necesitamos mucho)
BLANCO = (255, 255, 255)

# Tamaño de la ventana
TAMAÑO_VENTANA = 300
ANCHO_CELDA = TAMAÑO_VENTANA // 3

# Crear la ventana
ventana = pygame.display.set_mode((TAMAÑO_VENTANA, TAMAÑO_VENTANA))
pygame.display.set_caption("Ta-Te-Ti con IA")

# Cargar imágenes del tablero, cruz y círculo
imagen_tablero = pygame.image.load("/Users/facue/Desktop/Cursos/Proyectos de programacion/Ta_Te_Ti/IMG/tablero.png")
imagen_cruz = pygame.image.load("/Users/facue/Desktop/Cursos/Proyectos de programacion/Ta_Te_Ti/IMG/cruz.png")
imagen_circulo = pygame.image.load("/Users/facue/Desktop/Cursos/Proyectos de programacion/Ta_Te_Ti/IMG/circulo.png")

# Redimensionar las imágenes para que encajen en la ventana y las celdas
imagen_tablero = pygame.transform.scale(imagen_tablero, (TAMAÑO_VENTANA, TAMAÑO_VENTANA))
imagen_cruz = pygame.transform.scale(imagen_cruz, (ANCHO_CELDA, ANCHO_CELDA))
imagen_circulo = pygame.transform.scale(imagen_circulo, (ANCHO_CELDA, ANCHO_CELDA))

# Definir el tablero inicial como una lista con 9 espacios vacíos
tablero = [' ' for _ in range(9)]

# Función para dibujar el tablero en la ventana
def dibujar_tablero():
    # Dibujar la imagen del tablero
    ventana.blit(imagen_tablero, (0, 0))
    
    # Dibujar cruces y círculos en el tablero
    for i in range(9):
        fila = i // 3
        columna = i % 3
        x = columna * ANCHO_CELDA
        y = fila * ANCHO_CELDA
        
        if tablero[i] == 'X':
            ventana.blit(imagen_cruz, (x, y))
        elif tablero[i] == 'O':
            ventana.blit(imagen_circulo, (x, y))

# Función para verificar si hay un ganador
def hay_ganador(tabla, jugador):
    # Todas las posibles combinaciones ganadoras
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columnas
        [0, 4, 8], [2, 4, 6] # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tabla[combinacion[0]] == tabla[combinacion[1]] == tabla[combinacion[2]] == jugador:
            #== jugador: Verifica si todas estas posiciones contienen el símbolo del jugador actual.
            return True
    return False

# Función para verificar si el tablero está lleno
def tablero_lleno(tabla):
    return ' ' not in tabla

# Implementación del algoritmo Minimax 
def evaluar(tabla):
    if hay_ganador(tabla, 'O'): # IA puede ganar
        return 1
    elif hay_ganador(tabla, 'X'): # Jugador puede ganar
        return -1
    else: # puede empatar
        return 0

# Implementación del algoritmo Minimax
def minimax(tabla, profundidad, esMaximizingPlayer):#La tabla es el tablero. La profundidad es la
    #capacidad de ver los movimientos futuros. esMaximizingPlayer si es el jugador o la IA
    if hay_ganador(tabla, 'O') or hay_ganador(tabla, 'X') or tablero_lleno(tabla):
        return evaluar(tabla)
    
    if esMaximizingPlayer:# Si es True se ejecuta este codigo si no se ejecuta el otro
        #la IA (que intenta maximizar el valor de sus movimientos)
        mejor_valor = -math.inf # - infinito
        for i in range(9):
            if tabla[i] == ' ':
                tabla[i] = 'O' # La IA juega
                valor = minimax(tabla, profundidad + 1, False)#Invoca recursivamente el minimax
                #Una funcion recursiva es una funcion que se repite en cada celda vasia
                '''profundidad + 1: La profundidad se 
                incrementa, lo que significa que estamos analizando un movimiento futuro.
                False: Indica que en el siguiente nivel de la recursión será el turno del jugador humano
                (Minimizing Player).'''
                tabla[i] = ' '
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        #el jugador humano (que intenta minimizar las opciones de la IA)
        mejor_valor = math.inf
        for i in range(9):
            if tabla[i] == ' ':
                tabla[i] = 'X' # El jugador juega
                valor = minimax(tabla, profundidad + 1, True)
                tabla[i] = ' '
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor

# Función para la IA (jugador 'O') que utiliza Minimax
def mejor_movimiento_ia(tabla):
    mejor_valor = -math.inf
    mejor_movimiento = None
    for i in range(9):
        if tabla[i] == ' ':
            tabla[i] = 'O'
            valor = minimax(tabla, 0, False)
            tabla[i] = ' '
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = i
    return mejor_movimiento

# Función para manejar los eventos del juego
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
