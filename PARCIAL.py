# parcial juan sebastian gallego
import random # SE IMPORTA LA LIBRERIA RANDOM PARA SACAR LOS GOLES DE FORMA ALEATORIA DE LOCAL Y VISITANTE

# lista equipo local
lista_Equipo_local = [" Aguilas doradas ", " Millonarios ", " America ", " Boyaca chico "," Alianza Petrolera ", " Atlético Nacional ", " Atlético Junior ", " Independiente Santa Fe", "  Deportivo Pasto ", " Independiente Medellín ", " La Equidad ", " Envigado FC ", " Deportes Tolima ", " Jaguares de Córdoba ", " Deportivo Pereira ", " Atlético Huila ", " Deportivo Cali ", " Unión Magdalena ", " Atlético Bucaramanga ", " Once Caldas "]
print(lista_Equipo_local)    # se imprime lista equipos locales por consola

# lista equpo visitante
lista_Equipo_Visitante = [" Aguilas doradas ", " Millonarios ", " America ", " Boyaca chico "," Alianza Petrolera ", " Atlético Nacional ", " Atlético Junior ", " Independiente Santa Fe", "  Deportivo Pasto ", " Independiente Medellín ", " La Equidad ", " Envigado FC ", " Deportes Tolima ", " Jaguares de Córdoba ", " Deportivo Pereira ", " Atlético Huila ", " Deportivo Cali ", " Unión Magdalena ", " Atlético Bucaramanga ", " Once Caldas "]
print(lista_Equipo_Visitante)    # se imprime lista por consola de equipos visitantes 

#  lista de goles equipo local usando un random de 0 a 5
lista_Goles_Equipo_local = [random.randint(0, 5) for equipo in lista_Equipo_local]

# Accediendo a los datos
for i, equipoLocal in enumerate(lista_Equipo_local): # SE REALIZA UN FOR PARA MOSTRAR LOS GOLES POR EQUIPOS
    golesEquipoLocal = lista_Goles_Equipo_local[i] # Se obtiene la información de los goles para el equipo
    print(f"Goles de equipo local {equipoLocal}: {golesEquipoLocal}") # SE IMPRIME LOS GOLES POR EQUIPO


#  lista de goles equipo visitante usando un random de 0 a 5
lista_Goles_Equipo_Visitante = [random.randint(0, 5) for equipo in lista_Equipo_Visitante]

# Accediendo a los datos
for i, equipoVisitante in enumerate(lista_Equipo_Visitante): # SE REALIZA UN FOR PARA MOSTRAR LOS GOLES POR EQUIPOS VISITANTES
    golesEquipoVisitante = lista_Goles_Equipo_Visitante[i] # Se obtiene la información de los goles para el equipo visitante
    print(f"Goles de equipo visitante {equipoVisitante}: {golesEquipoVisitante}") # SE IMPRIME LOS GOLES POR EQUIPO



# lista general con todos los equipos 
    lista_Equipos_total = [" Aguilas doradas ", " Millonarios ", " America ", " Boyaca chico "," Alianza Petrolera ", " Atlético Nacional ", " Atlético Junior ", " Independiente Santa Fe", "  Deportivo Pasto ", " Independiente Medellín ", " La Equidad ", " Envigado FC ", " Deportes Tolima ", " Jaguares de Córdoba ", " Deportivo Pereira ", " Atlético Huila ", " Deportivo Cali ", " Unión Magdalena ", " Atlético Bucaramanga ", " Once Caldas "]

# Genera una lista aleatoria para indicar si el equipo juega de local o visitante
partidos_liga = len(lista_Equipos_total)
local_visitante = [random.randint(0, 1) for _ in range(partidos_liga)]

# Se obtiene los índices de los equipos
indices_equipos_liga = list(range(len(lista_Equipos_total)))

# Mezclar los índices aleatoriamente
random.shuffle(indices_equipos_liga)

# Se le asigna a cada equipo si juega de local o visitante según los índices mezclados
equipos_local = [lista_Equipos_total[i] for i in indices_equipos_liga[:partidos_liga//2]]
equipos_visitante = [lista_Equipos_total[i] for i in indices_equipos_liga[partidos_liga//2:]]

# Imprimir los equipos que juegan de local y visitante
print("Equipos que juegan de local:", equipos_local)
print("Equipos que juegan de visitante:", equipos_visitante)







