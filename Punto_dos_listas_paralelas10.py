# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 10. Equipo que más goles realizó

# Lista de equipos total de la liga 
lista_equipos_liga = ["Aguilas doradas", "Millonarios", "America", "Boyaca chico", "Alianza Petrolera","Atlético Nacional", "Atlético Junior", "Independiente Santa Fe", "Deportivo Pasto","Independiente Medellín", "La Equidad", "Envigado FC", "Deportes Tolima", "Jaguares de Córdoba","Deportivo Pereira", "Atlético Huila", "Deportivo Cali", "Unión Magdalena", "Atlético Bucaramanga", "Once Caldas"]


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

#se crea diccionario vacío para almacenar los goles de los equipos de la liga
goles_por_equipo_liga = {}

# se recorre sobre los resultados de partidos quien es el de mayor goles
#se asigna el equipo local y el equipo visitante a las variables equipo_local y equipo_visitante
# y se asignan los goles marcados por cada equipo a las variables goles_local y goles_visitante
for partido in resultados:
    equipo_local = partido[0]
    equipo_visitante = partido[1]
    goles_local = partido[2]
    goles_visitante = partido[3]
    
    #se verifica si el equipo local ya está en el diccionario goles_por_equipo_liga. Si no está se agrega con el número de goles
    #  marcados en el partido actual si ya está se suma el número de goles marcados en el partido actual al 
    # número existente de goles marcados
    if equipo_local not in goles_por_equipo_liga:
        goles_por_equipo_liga[equipo_local] = goles_local
    else:
        goles_por_equipo_liga[equipo_local] += goles_local
    
    if equipo_visitante not in goles_por_equipo_liga:
        goles_por_equipo_liga[equipo_visitante] = goles_visitante
    else:
        goles_por_equipo_liga[equipo_visitante] += goles_visitante

# se obtiene el equipo con mayor goles en la liga
equipo_max_goles_liga = max(goles_por_equipo_liga, key=goles_por_equipo_liga.get)

# se imprima el equipo con mayor goles 
print("El equipo que más goles realizó es:", equipo_max_goles_liga, "con un total de", goles_por_equipo_liga[equipo_max_goles_liga], "goles en la liga.")