# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 11. Equipo que menos goles recibió

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

#se crea diccionario vacío para almacenar los goles recibidos
goles_recibidos_liga = {}

# se recorre sobre los resultados de partidos cual es el
#equipo que menos goles recibió como visitante, se asignan al equipo
#visitando y los goles que recibió
for partido in resultados:
    equipo_visitante = partido[1]
    goles_visitante = partido[3]
    
    #se realiza condición para verificar cual es el equipo que menos goles recibió
    if equipo_visitante not in goles_recibidos_liga:
        goles_recibidos_liga[equipo_visitante] = goles_visitante
    else:
        goles_recibidos_liga[equipo_visitante] += goles_visitante

#se obtiene el equipo con menor goles recibidos
equipo_menos_goles_recibidos = min(goles_recibidos_liga, key=goles_recibidos_liga.get)

#se imprime el equipo con menos goles recibidos como visitante
print("Equipo que menos goles recibió como visitante:", equipo_menos_goles_recibidos)