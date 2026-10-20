# Desarrolla un programa que lea el número de aciertos y de errores obtenidos en un juego de preguntas. Cada acierto suma 3 puntos y cada error resta 1 punto.

ACIERTO: int = 3
ERROR: int = -1

VALORACION_PARTIDA: tuple[str, str, str] = ("Sigue practicando", "Buen resultado", "Excelente")



def calcular_resultados(aciertos: int, errores: int) -> tuple[int, int]:
    """
    Calcula el número total de preguntas respondidas y la puntuación.

    Args:
    aciertos = Número de aciertos
    errores = Número de errores

    Returns:
    tuple[int, int] = Preguntas en total, Puntuación

    """

    preguntas_total: int = aciertos + errores

    puntuacion: int = (aciertos * ACIERTO) + (errores * ERROR)

    return preguntas_total, puntuacion



def valorar_partida(puntuacion: int) -> int:
    """
    Calcula la valoración.

    Args:
    puntuacion = Puntuación total de la partida

    Returns:
    int = Índice del mensaje VALORACION_PARTIDA
    
    """

    if puntuacion < 10:
        return 0
    elif puntuacion >= 10 and puntuacion <= 19:
        return 1
    else:
        return 2



def main():
    """
    Función principal

    Args:
    Número de aciertos en las preguntas
    Número de errores en las preguntas

    Returns:
    Número de preguntas respondidas en total
    Puntuación
    Valoración
    
    """

    # Entrada

    aciertos = int(input())
    errores = int(input())

    # Salida

    if aciertos < 0 or errores < 0:
        print("ERROR - valores incorrectos")
    else:
        preguntas_total, puntuacion = calcular_resultados(aciertos, errores)
        indice_valoracion = valorar_partida(puntuacion)

        print(f"Preguntas respondidas: {preguntas_total}")
        print(f"Puntuación: {puntuacion}")
        print(f"Valoración: {VALORACION_PARTIDA[indice_valoracion]}")

if __name__ == "__main__":
    main()