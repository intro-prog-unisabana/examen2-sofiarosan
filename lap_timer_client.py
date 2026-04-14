# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    archivo = input()

    # Abrir archivo
    with open(archivo, 'r') as f:
        # Leer número de vueltas
        n = int(f.readline())

        # Crear cronómetro
        cronometro = lap_timer.init(n)

        # Leer los tiempos y agregarlos
        for _ in range(n):
            tiempo = float(f.readline())
            lap_timer.add_lap(cronometro, tiempo)

    # Calcular racha decreciente
    racha = lap_timer.longest_decreasing_streak(cronometro)

    print(racha)

if __name__ == "__main__":
    main()
