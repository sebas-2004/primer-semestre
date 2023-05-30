# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 9. Listado de los equipos con sus goles de local y visitante

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


# se crean diccionarios vacíos para almacenar los goles de los equipos de la liga
goles_local = {}
goles_visitante = {}

# se recorre sobre los resultados de partidos y sumar los goles de los equipos local y visitante
for partido in resultados:
    equipo_local = partido[0]
    equipo_visitante = partido[1]
    goles_equipo_local = partido[2]
    goles_equipo_visitante = partido[3]
    
    if equipo_local not in goles_local: # se realiza condicionales si tiene goles de visitante o local
        goles_local[equipo_local] = 0
    if equipo_visitante not in goles_visitante:
        goles_visitante[equipo_visitante] = 0
        
    goles_local[equipo_local] += goles_equipo_local
    goles_visitante[equipo_visitante] += goles_equipo_visitante

# se recorre sobre la lista de equipos y obtener los goles de local y visitante
for equipo in lista_equipos_liga:
    goles_local_equipo = goles_local.get(equipo, 0)
    goles_visitante_equipo = goles_visitante.get(equipo, 0)
    
    #se imprime el equipo con la cantidad de goles local y visitante
    print(f"{equipo}: Goles de local = {goles_local_equipo}, Goles de visitante = {goles_visitante_equipo}")