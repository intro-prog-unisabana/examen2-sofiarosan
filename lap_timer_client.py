# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    #  Pedir el nombre del archivo al usuario usando input()
    archivo=input()
    #  Abrir el archivo y leer el numero de vueltas n
    with open(archivo, 'r') as f:
        n= int(f.readline())
    #  Crear el cronometro usando lap_timer.init(n)
        cronometro = lap_timer.init(n)
    # Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
        
    # Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()


if __name__ == "__main__":
    main()
