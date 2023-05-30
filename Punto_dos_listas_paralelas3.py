# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 3. Calcular cantidad partidos perdidos por equipo

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

# Se inicializa las listas de partidos ganados y partidos perdidos en la liga
#Cada lista tiene una lontitud igual a la lista de equipos
ganados_liga = [0] * len(lista_equipos_liga)
perdidos_liga = [0] * len(lista_equipos_liga)

# Iterar sobre la lista de resultados de partidos
# En cada iteración se obtiene el nombre y resultado de los equipos
for resultado in resultados:
    equipo1 = resultado[0]
    equipo2 = resultado[1]
    resultado1 = resultado[2]
    resultado2 = resultado[3]

    # se actualizan los partidos ganados y partidos perdidos por cada equipo en la liga
    if resultado1 > resultado2: 
        ganados_liga[lista_equipos_liga.index(equipo1)] += 1
        perdidos_liga[lista_equipos_liga.index(equipo2)] += 1
    elif resultado2 > resultado1:
        ganados_liga[lista_equipos_liga.index(equipo2)] += 1
        perdidos_liga[lista_equipos_liga.index(equipo1)] += 1
    else:
        # cuando no hay empate no se actualiza la lista
        pass

# Se imprime los resultados de cada equipo con la cantidad de partidos perdidos
for i in range(len(lista_equipos_liga)): # Se realiza un ciclo for para mostrar uno a uno los partidos perdidos de cada equipo
    print(f"{lista_equipos_liga[i]}: {perdidos_liga[i]} partidos perdidos en la liga")