# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 

# 1. Calcular cantidad partidos por equipo

# Lista de equipos total de la liga 
lista_equipos_liga = ["Aguilas doradas", "Millonarios", "America", "Boyaca chico", "Alianza Petrolera","Atlético Nacional", "Atlético Junior", "Independiente Santa Fe", "Deportivo Pasto","Independiente Medellín", "La Equidad", "Envigado FC", "Deportes Tolima", "Jaguares de Córdoba","Deportivo Pereira", "Atlético Huila", "Deportivo Cali", "Unión Magdalena", "Atlético Bucaramanga", "Once Caldas"]

# se genera una lista aleatoria  para indicar si el equipo juega de local o visitante
partidos = len(lista_equipos_liga) * 20 # los equipos juegan de a 20 partidos
local_visitante = [random.randint(0, 1) for _ in range(partidos)]

# se inicializa la lista para contar cantidad de partidos de cada equipo
cantidad_partidos = [0] * len(lista_equipos_liga)

# Contar cantidad de partidos de cada equipo
for i in range(len(local_visitante)):
    equipo_index = i // 20 # se obtiene índice del equipo (cada equipo tiene 20 partidos)
    if local_visitante[i] == 0:
        cantidad_partidos[equipo_index] += 1 # se suma 1 si el equipo juega de local en la liga
    else:
        cantidad_partidos[equipo_index] += 1 # se suma 1 si el equipo juega de visitante en la liga

# Imprimir la cantidad de partidos de cada equipo en la liga recorriendo un ciclo for
for i in range(len(lista_equipos_liga)):
    print("El equipo "+ lista_equipos_liga[i] + ", jugó ", cantidad_partidos[i], "partidos")