# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 4. Calcular cantidad partidos empatados por equipo

# Lista de equipos de la liga
lista_equipos_liga = ["Aguilas doradas", "Millonarios", "America", "Boyaca chico", "Alianza Petrolera",
                 "Atlético Nacional", "Atlético Junior", "Independiente Santa Fe", "Deportivo Pasto",
                 "Independiente Medellín", "La Equidad", "Envigado FC", "Deportes Tolima", "Jaguares de Córdoba",
                 "Deportivo Pereira", "Atlético Huila", "Deportivo Cali", "Unión Magdalena",
                 "Atlético Bucaramanga", "Once Caldas"]

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

# se crean listas para partidos jugados y partidos empatados
partidos_jugados_liga = [0] * len(lista_equipos_liga)
partidos_empatados_liga = [0] * len(lista_equipos_liga)

# se recorre la lista de resultados de partidos
# En cada iteración se obtiene el nombre y resultado de los equipos
for resultado in resultados:
    equipo_local = resultado[0]
    equipo_visitante = resultado[1]
    goles_local = resultado[2]
    goles_visitante = resultado[3]
    
    # Encontrar los índices de los equipos en la lista de equipos
    indice_local = lista_equipos_liga.index(equipo_local)
    indice_visitante = lista_equipos_liga.index(equipo_visitante)
    
    # se actualiza la cantidad de partidos jugados por cada equipo en la liga
    partidos_jugados_liga[indice_local] += 1
    partidos_jugados_liga[indice_visitante] += 1
    
    # se actualiza la cantidad de partidos empatados por cada equipo en la liga
    if goles_local == goles_visitante:
        partidos_empatados_liga[indice_local] += 1
        partidos_empatados_liga[indice_visitante] += 1

# se imprime la cantidad de partidos empatados por cada equipo en la liga
for i in range(len(lista_equipos_liga)): # Se realiza un ciclo for para mostrar uno a uno los partidos empatados de cada equipo
    equipo = lista_equipos_liga[i]
    partidos_empatados_equipo = partidos_empatados_liga[i]
    print(f"{equipo}: {partidos_empatados_equipo} partidos empatados en la liga")