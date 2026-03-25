import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def calcular_pasos_kaprekar(n):
    """Calcula los pasos (0-7) para llegar a 6174 o retorna -1 si es inválido."""
    s_num = str(n).zfill(4)
    if len(set(s_num)) <= 1:
        return -1 # Caso de dígitos iguales (ej. 1111)

    actual = n
    pasos = 0
    while actual != 6174:
        s = str(actual).zfill(4)
        grande = int("".join(sorted(s, reverse=True)))
        pequeno = int("".join(sorted(s)))
        actual = grande - pequeno
        pasos += 1
        if pasos > 7: break
    return pasos

def generar_visualizacion_kaprekar(n_max):
    # Definimos el tamaño de la matriz (ej. 100x100 para n=10000)
    lado = int(np.ceil(np.sqrt(n_max)))
    matriz = np.zeros((lado, lado))

    for i in range(n_max):
        pasos = calcular_pasos_kaprekar(i)
        fila = i // lado
        columna = i % lado
        matriz[fila, columna] = pasos

    # --- PALETA DE COLORES PERSONALIZADA ---
    # -1: Blanco (Inválidos/Agujeros)
    # 0: Gris muy claro (La constante 6174)
    # 1-7: Tu paleta + 3 colores armoniosos
    colores_hex = [
      '#ffffff', # -1: Blanco (Números inválidos - "vacíos")
      '#f2f2f2', #  0: Gris seda (La constante 6174, casi blanco)
      '#faa4b5', #  1: Rosa (Tu origen)
      '#f8b77c', #  2: Naranja (Tu origen)
      '#fff184', #  3: Amarillo (Tu origen)
      '#93d29b', #  4: Verde Menta (Puente armonioso entre amarillo y azul)
      '#b19cd9', #  5: Lavanda (Sustituye al morado oscuro para dar suavidad)
      '#70c1e1', #  6: Azul Cielo (Más vibrante que el oscuro, menos pesado)
      '#c4e7f7', #  7: Azul Hielo (Tu azul final)
    ]
    cmap_custom = ListedColormap(colores_hex)

    # Crear el gráfico
    plt.figure(figsize=(12, 12), facecolor='white')
    plt.imshow(matriz, cmap=cmap_custom, origin='lower', interpolation='nearest')

    # Estética del gráfico
    plt.title(f"Tapiz de Kaprekar: Pasos para {n_max} números", fontsize=16, pad=20)
    plt.axis('off') # Quitamos los ejes para que parezca una obra de arte

    # Barra de color con etiquetas claras
    cbar = plt.colorbar(ticks=range(-1, 8), fraction=0.046, pad=0.04)
    cbar.ax.set_yticklabels(['Inválido', '0 pasos', '1 paso', '2', '3', '4', '5', '6', '7'])

    plt.show()

# Ejecutar para los primeros 10,000 números (Matriz 100x100)
generar_visualizacion_kaprekar(10000)