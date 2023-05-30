# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM 
#import matplotlib.pyplot as plt

# 5. Calcular cantidad de goles de los equipos locales

# Lista de equipos de la liga
lista_Equipo_local = [" Aguilas doradas ", " Millonarios ", " America ", " Boyaca chico "," Alianza Petrolera ", " Atlético Nacional ", 
                      " Atlético Junior ", " Independiente Santa Fe", "  Deportivo Pasto ", " Independiente Medellín ", " La Equidad ",
                        " Envigado FC ", " Deportes Tolima ", " Jaguares de Córdoba ", " Deportivo Pereira ", " Atlético Huila ", 
                        " Deportivo Cali ", " Unión Magdalena ", " Atlético Bucaramanga ", " Once Caldas "]


# se crea una lista paralela con la cantidad de goles de cada equipo en cada partido
lista_goles = [[random.randint(0, 5) for _ in range(10)] for _ in range(len(lista_Equipo_local))]

# se calcula la cantidad total de goles de cada equipo
goles_locales = [sum(lista_goles[i]) for i in range(len(lista_Equipo_local))]

# se imprime la cantidad de goles de cada equipo local
for i in range(len(lista_Equipo_local)):
    print("Equipo local", lista_Equipo_local[i] + ": " + str(goles_locales[i]), "goles")
