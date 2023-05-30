
# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 13. Lea por teclado el nombre del equipo y liste los partidos en lo que ha participado y sus marcadores
# 14. imprimir tabla de posiciones de mayor a menor puntaje

# se llena una lista con los resultados de los partidos
resultados = [["Millonarios", "Deportivo Cali", 2, 1],
              ["Atlético Nacional", "Alianza Petrolera", 3, 0],
              ["Millonarios", "Deportivo Pasto", 1, 0],
              ["Atlético Junior", "Deportivo Cali", 2, 2],
              ["Independiente Santa Fe", "Atlético Nacional", 1, 0],
              ["Millonarios", "Jaguares de Córdoba", 3, 1],
              ["Atlético Bucaramanga", "Deportivo Cali", 0, 1],
              ["Independiente Medellín", "La Equidad", 2, 0],
              ["Atlético Nacional", "Envigado FC", 1, 0],
              ["Millonarios", "Deportivo Pereira", 2, 0],
              ["Once Caldas", "Atlético Nacional", 1, 0],
              ["Deportivo Cali", "Boyaca chico", 2, 1],
              ["Millonarios", "Independiente Santa Fe", 0, 1],
              ["Atlético Nacional", "Deportes Tolima", 2, 1],
              ["La Equidad", "Millonarios", 0, 0],
              ["Alianza Petrolera", "Atlético Nacional", 0, 0],
              ["Deportivo Cali", "Unión Magdalena", 1, 0],
              ["Deportivo Pasto", "Atlético Huila", 2, 0],
              ["Atlético Nacional", "Deportivo Cali", 1, 1],
              ["Envigado FC", "Millonarios", 2, 0]]


# Calcular puntos por equipo
#almacena la cantidad de puntos obtenidos por los equipos
puntos_por_equipo_liga = {}

#se recorre la lista resuktados y se agregan los puntos a cada equipo
#de acuerdo a los resultados de los partidos
for partido in resultados:
    equipo_local = partido[0]
    equipo_visitante = partido[1]
    goles_local = partido[2]
    goles_visitante = partido[3]
    
    #se realiza condiciones de si el equipo local o visitante ganó o empató
    if goles_local > goles_visitante:
        # Equipo local ganó
        if equipo_local not in puntos_por_equipo_liga:
            puntos_por_equipo_liga[equipo_local] = 3
        else:
            puntos_por_equipo_liga[equipo_local] += 3
        if equipo_visitante not in puntos_por_equipo_liga:
            puntos_por_equipo_liga[equipo_visitante] = 0
        else:
            puntos_por_equipo_liga[equipo_visitante] += 0
    elif goles_local < goles_visitante:
        # Equipo visitante ganó
        if equipo_visitante not in puntos_por_equipo_liga:
            puntos_por_equipo_liga[equipo_visitante] = 3
        else:
            puntos_por_equipo_liga[equipo_visitante] += 3
        if equipo_local not in puntos_por_equipo_liga:
            puntos_por_equipo_liga[equipo_local] = 0
        else:
            puntos_por_equipo_liga[equipo_local] += 0
    else:
        # Empate entre los equipos
        if equipo_local not in puntos_por_equipo_liga:
            puntos_por_equipo_liga[equipo_local] = 1
        else:
            puntos_por_equipo_liga[equipo_local] += 1
        if equipo_visitante not in puntos_por_equipo_liga:
            puntos_por_equipo_liga[equipo_visitante] = 1
        else:
            puntos_por_equipo_liga[equipo_visitante] += 1

# se crea lista de equipos ordenados por puntos
tabla_posiciones = sorted(puntos_por_equipo_liga.items(), key=lambda x: x[1], reverse=True)

# se imprime tabla de posiciones de mayor a menor úntaje
print("Tabla de Posiciones de mayor a menor puntaje")
print("-------------------")
print("{:<20} | {:<10}".format("Equipo liga", "Puntos"))
print("-------------------")
# se recorreo la tabla de posiciones para imprimir los equipos con los puntos
for equipo, puntos in tabla_posiciones:
    print("{:<20} | {:<10}".format(equipo, puntos))


