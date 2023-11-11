from os import system
import time
import random


def reglas():
    """Esta funcion imprime por pantalla las reglas del blackjat."""
    system("cls")
    print("Objetivo del juego:\n\n- Conseguir 21 puntos o plantarse con más puntos que el otro jugador.")
    print("- Si el jugador se pasa de 21, pierde automáticamente.")
    print("- Si nadie se pasa, gana el jugador con la mano más cercana a 21.")
    print("- Una vez te pases de 21 no podrás volver a pedir otra carta.")
    print("- Se repartirá una carta por jugador y en la primera ronda se deberá pedir otra carta obligatoriamente.")
    print("- Una vez pasada la primera ronda los jugadores podrán plantarse cuando quieran.")
    print("- Las cartas numéricas valen su número, las figuras valen 10 y el As puede valer 1 u 10.\n")
    print("- Pulsa enter para volver al menu.")
    input()
    system("cls")
    menu()


def nombres(rondas_ganadas_jugador1,rondas_ganadas_jugador2, tipo_partida):
    """Pide los nombres de los jugadores que van ha jugar cada partida y comienza la partida."""
    if tipo_partida == 1: # Si la partida es del modo un jugador preguntará el nombre del jugador y comenzará la partida para un jugador
        nombre=input("¿Quién va a ser el jugador? ").capitalize()
        nombre2= "Diego"
        jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)
    if tipo_partida == 2: # Si la partida es del modo dos jugadores preguntará el nombre de los jugadores y comenzará la partida para dos jugadores
        nombre=input("¿Quién va a ser el jugador 1? ").capitalize()
        nombre2=input("¿Quién va a ser el jugador 2? ").capitalize()
        jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)


def numero_aleatorio():
    """Da valor aleatorio entre 0 y 12 y almacena en la variable numero y lo retorna"""
    numero=random.randint(0,12)
    return numero


def pedir_carta(numero):
    """Da una carta dependiendo del numero aleatorio que haya salido en la función numero_aleatorio() y retorna la variable carta"""
    numero2 = numero
    baraja = "A234567890JKQ"
    carta = baraja[numero2] # Carta corresponde a un caracter aleatorio de las posiciones 0 y 12 de baraja 
    return carta


def suma_cartas(cartas):
    """Comprueba las cartas del jugador y las suma una a una dependiendo de las cartas que tenga el jugador y retorna las sumas de las cartas."""
    contador= 0
    suma_carta=0
    for i in range (1,(len(cartas)+1)): 
        # El bucle se ejecutara carta por carta que tenga en la mano, si en la mano del jugador hay una A, J, K, Q, o 0 le dará el valor de 10 a la suma
        una_carta = cartas[contador]
        if una_carta == "A":
            suma_carta+=10
        elif una_carta == "J":
            suma_carta+=10
        elif una_carta == "K":
            suma_carta+=10
        elif una_carta=="Q":
            suma_carta+=10
        elif una_carta=="0":
            suma_carta+=10
        else: # Si no hay ningua de las letras anteriores en las cartas del jugador se sumarán las cartas por su valor correspondiente
            suma_carta+=int(una_carta)
        contador+=1
    if suma_carta > 21: # Si la suma de las cartas es mayor a 21 y hay un a A en las cartas dle jugador se le restará 9 a las suma de las cartas para que el A valga 1 en lugar de 10
        if "A" in cartas:
            suma_carta-=9
    return suma_carta


def final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2):
    """Imprime las rondas que han ganado los jugadores y pregunta si se quiere volver al menú o si quiere finalizar el programa."""
    system("cls")
    print("El jugador "+ nombre+" ganado un total de: " + str(rondas_ganadas_jugador1)+ " rondas")
    print("El jugador "+ nombre2+" ganado un total de: " + str(rondas_ganadas_jugador2)+ " rondas")
    while_menu=0
    while while_menu == 0:
        volver_menu=input("¿Quieres volver al menú?(S/N) ").upper() # Pide al jugador si quiere volver al menú
        if volver_menu == "S": # Si escribe S se ejecutará la función menu() y volverá al menú
            system("cls")
            menu()
            while_menu = 1
        elif volver_menu== "N": # Si escribe N, el programa finalizará 
            system("cls")
            print("Gracias por jugar a nuestro Blackjack.")
            print("Trabajo desarrollado por Nicolás De Gomar Almellones e Iván López Jiménez\n")
            print("Programa finalizado, dale enter para cerrar la ventana.")
            input()
            system("cls")
            exit()
        else: # Si introduce un caracter erróneo dará error y lo pedirá de nuevo
            print("ERROR - INTRODUCE UN DIGITO VALIDO")


def animaciones():
    """Ejecuta las animaciones para cuando se reparten las cartas a los jugadores."""
    system("cls")
    print("Se están repartiendo las cartas.\n")
    print("*\n")
    time.sleep(0.3)
    print("**\n")
    time.sleep(0.3)
    print("***\n")
    time.sleep(0.3)
    print("****\n")
    time.sleep(0.3)


def jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida):
    """Ejecuta la partida para un jugador hasta que no se quiera jugar más.\n
        Son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas"""
    pedir = ""
    pedir2 = "S"
    ronda2 = 1
    plantarse="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    numero = numero_aleatorio()
    cartas_jugador+=pedir_carta(numero) # Se le da una carta al jugador 1
    numero = numero_aleatorio()
    cartas_jugador2+=pedir_carta(numero) # Se le da una carta a la máquina
    system("cls")
    # Empieza la primera ronda con la primera carta de cada jugador entregada y donde se deberá pedir otra carta obligatoriamente
    while len(cartas_jugador) < 2: # Mientras el jugador 1 solo tenga un carta se ejecutara el bucle
        animaciones() 
        # Se ejecutan las animaciones de repartir las cartas y  despues imprime las cartas de cada jugador
        system("cls")
        print(f"RONDA {ronda2}")
        print(nombre +" tus carta son: "+cartas_jugador+" ("+str(suma_cartas(cartas_jugador))+")")
        print("Las cartas de "+ nombre2+" son: "+cartas_jugador2+" ("+str(suma_cartas(cartas_jugador2))+")")
        pedir=input("¿Quieres pedir una carta más(S) o plantarte(N)? ").upper() 
        # Pregunta si quiere una carta o no, en este caso el jugador debe pedir una carta obligatoriamente,
        #  por lo que si no lo hace da un error.
        if pedir == "S": # Si el jugador pide una carta se le dará una carta más y saldrá del bucle
            ronda2 = ronda1(ronda2) # Llama a la función ronda1()
            numero = numero_aleatorio()
            cartas_jugador+=pedir_carta(numero)
            numero = numero_aleatorio()
            cartas_jugador2+=pedir_carta(numero)
        else: # Si el jugador no pide una carta dará error y empezará de nuevo el bucle
            print("ERROR EN EL PRIMER TURNO DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    while plantarse == "S" and suma_cartas(cartas_jugador)<22:  
    # Una vez terminada la primera ronda donde se debe pedir obligatoriamente se borra la pantalla
    # y entra en un bucle donde se jugarán las demás rondas hasta que el jugador se plante 
    # o el jugador o la máquina se pasen de 21
        animaciones()
        system("cls")
        print(f"RONDA {ronda2}")
        print(nombre +" tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿Quieres pedir una carta más(S) o plantarte(N)? ").upper() 
        # Pregunta si quiere una carta o no, al no ser obligatoria pedir otra carta más 
        # podrá elegir entre pedir otra carta o plantarse
        if pedir == "S":
            ronda2 = ronda1(ronda2)
            numero = numero_aleatorio()
            cartas_jugador+=pedir_carta(numero)
        if pedir == "N" and suma_cartas(cartas_jugador2) >= suma_cartas(cartas_jugador): 
                # Si el jugador se planta y la máquina tiene una suma mayor que el jugador la máquina se plantará tambien
                pedir2 = "N"
        if pedir2=="S" and suma_cartas(cartas_jugador2) <= 18: 
            # Si la suma de las cartas de la máquina es menor o igual a 18 irá sacando cartas
            numero = numero_aleatorio()
            cartas_jugador2+=pedir_carta(numero)
            if pedir=="N":
                ronda2 = ronda1(ronda2)
            while pedir=="N" and pedir2=="S" and suma_cartas(cartas_jugador2) < suma_cartas(cartas_jugador) : 
                # Si el jugador se planta y la máquina tiene menos que el jugador
                # seguirá sacando cartas hasta ser mayor que el jugador
                numero = numero_aleatorio()
                cartas_jugador2+=pedir_carta(numero)
                ronda2 = ronda1(ronda2)
        if pedir=="N":
            plantarse="N"
        if pedir != "S" and pedir != "N":
            input("ERROR. ENTER PARA INTENTARLO DE NUEVO")
    if suma_cartas(cartas_jugador)>21 or suma_cartas(cartas_jugador2)>21: 
        # Una vez el jugador 1 se plante si uno de los dos o los dos se pasan de 21 se ejecutará la función se_pasa()
        print(se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)) # Ejecuta la función e imprimirá quien se ha pasado 
        input("PULSA ENTER PARA VER RESULTADOS")
    print(resultado_texto(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)) 
    # Una vez terminada las rondas se llama a la función resultado_texto() y resultado para imprimir los resultados de la partida
    resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador, nombre, nombre2, tipo_partida)


def se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2):
    """Comprueba si alguno de los jugadores de la partida se ha pasado de 21 y si es correcto imprime el jugador que se ha pasado."""
    system("cls")
    if suma_cartas(cartas_jugador2) > 21 and suma_cartas(cartas_jugador) > 21: 
        # Si el jugador 2 y el jugador 1 se han pasado de 21 se imprime que se han pasado los dos
        return f"RONDA {str(ronda2)}\nJ1 - {nombre} - {cartas_jugador} **se pasa**\nJ2 - {nombre2} - {cartas_jugador2} **se pasa**"
    if suma_cartas(cartas_jugador2) > 21: # Si el jugador 2 se ha pasado de 21 se imprime que se ha pasado
        return f"RONDA {str(ronda2)}\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} **se pasa**"
    elif suma_cartas(cartas_jugador) > 21: # Si el jugador 1 se ha pasado de 21 se imprime que se ha pasado
        return f"RONDA {str(ronda2)}\nJ1 - {nombre} - {cartas_jugador} **se pasa**\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"    


def ronda1(ronda2): 
    """Suma las rondas que se van jugando."""
    ronda2 += 1
    return ronda2


def jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida):
    """Ejecuta la partida para dos jugadores hasta que no se quiera jugar más.\n
        Son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas"""
    pedir = ""
    pedir2 = ""
    ronda2 = 1
    plantarse_jugador1="S"
    plantarse_jugador2="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    numero = numero_aleatorio()
    cartas_jugador+=pedir_carta(numero) 
    numero = numero_aleatorio()
    cartas_jugador2+=pedir_carta(numero) 
    # Se le da un a carta al jugador 1 y luego al jugador 2,
    # se ejecutan las animaciones para repartir cartas y se imprime la primera carta que les ha salido a los dos
    animaciones()
    system("cls")
    print(f"RONDA {ronda2}")
    print("Las cartas de "+nombre+" son: "+cartas_jugador+" ("+str(suma_cartas(cartas_jugador))+")")
    print("Las cartas de "+nombre2+" son: "+cartas_jugador2+" ("+str(suma_cartas(cartas_jugador2))+")")
    input("ENTER PARA EMPEZAR")
    # Empieza la primera ronda donde cada jugador deberá pedir una carta obligatoriamente
    while len(cartas_jugador) < 2: # Mientras el jugador 1 solo tenga un carta se ejecutara el bucle
        system("cls")
        print(f"RONDA {ronda2}")
        print(nombre + " tus carta son: "+cartas_jugador+" ("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿Quieres pedir una carta más(S) o plantarte(N)? ").upper() 
        # Pregunta si quiere una carta o no, en este caso el jugador 
        # debe pedir una carta obligatoriamente por lo que si no lo hace da un error.
        if pedir == "S": # Si el jugador pide una carta se le dará una carta más y saldrá del bucle
            # se ejecutarán las animaciones y se le dará una carta más al jugador 1
            animaciones()
            numero = numero_aleatorio()
            cartas_jugador+=pedir_carta(numero)
        else: # Si el jugador no pide una carta dará error y empezará de nuevo el bucle
            print("ERROR EN EL PRIMER TURNO "+ nombre +  "DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    while len(cartas_jugador2) < 2: # Mientras el jugador 2 solo tenga un carta se ejecutara el bucle
        system("cls")
        print(f"RONDA {ronda2}")
        print(nombre2 + " tus cartas son: "+cartas_jugador2+" ("+str(suma_cartas(cartas_jugador2))+")")
        pedir2=input("¿Quieres pedir una carta más(S) o plantarte(N)? ").upper() # Pregunta si quiere una carta o no, en este caso el jugador debe pedir una carta obligatoriamente por lo que si no lo hace da un error.
        if pedir2 == "S": # Si el jugador pide una carta se le dará una carta más y saldrá del bucle
            # se ejecutarán las animaciones y se le dará una carta más al jugador 2
            animaciones()
            ronda2 = ronda1(ronda2) 
            numero = numero_aleatorio()
            cartas_jugador2+=pedir_carta(numero)
        else: # Si el jugador no pide una carta dará error y empezará de nuevo el bucle
            print("ERROR EN EL PRIMER TURNO "+ nombre2 +  " DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    system("cls") 
    fin = "S"
    # Una vez terminada la primera ronda donde se debe pedir obligatoriamente 
    # se borra la pantalla y entra en un bucle donde se jugarán las demás rondas 
    # hasta que los dos jugadores se planten o uno de los dos se pase de 21
    while fin == "S" and suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_jugador)<22: 
        while (plantarse_jugador1 == "S" and suma_cartas(cartas_jugador)<22) or (plantarse_jugador2 == "S"  and suma_cartas(cartas_jugador2)<22):
            # Primero pregunta al jugador uno si quiere una carta o plantarse
            if plantarse_jugador1 == "S" and suma_cartas(cartas_jugador)<22:
                pedir=""
                pedir2=""
                while pedir != "S" and pedir != "N":
                    system("cls")
                    print(f"RONDA {ronda2}")
                    print(nombre + " tus cartas son: "+cartas_jugador+" ("+str(suma_cartas(cartas_jugador))+")")
                    pedir=input("¿Quieres pedir una carta más(S) o plantarte(N)? ").upper()
                    if pedir == "S":
                        animaciones()
                        numero_aleatorio()
                        cartas_jugador+=pedir_carta(numero)
                    elif pedir=="N":
                        plantarse_jugador1="N"
                    elif pedir != "S" and pedir != "N":
                        input("ERROR. ENTER PARA INTENTARLO DE NUEVO")
                pedir=""
            # Ahora pregunta al jugador dos si quiere una carta o plantarse
            if plantarse_jugador2 == "S" and suma_cartas(cartas_jugador2)<22:
                while pedir2 != "S" and pedir2 != "N":
                    system("cls")
                    print(f"RONDA {ronda2}")
                    print(nombre2 + " tus cartas son: "+cartas_jugador2+" ("+str(suma_cartas(cartas_jugador2))+")")
                    pedir2=input("¿Quieres pedir una carta más(S) o plantarte(N)? ").upper()
                    if pedir2 == "S":
                        animaciones()
                        numero= numero_aleatorio()
                        cartas_jugador2+=pedir_carta(numero)
                    elif pedir2=="N":
                        plantarse_jugador2="N"
                    elif pedir2 != "S" and pedir != "N":
                        input("ERROR. ENTER PARA INTENTARLO DE NUEVO")
                pedir2=""
            # Si los jugadores van pidiendo cartas se le irá sumando uno a las rondas 
            # despues de preguntar a los dos o a uno en caso de que uno se haya plantado
            if plantarse_jugador1 == "S" or plantarse_jugador2 == "S":
                ronda2 = ronda1(ronda2)
        if suma_cartas(cartas_jugador2)>21 or suma_cartas(cartas_jugador)>21:
            # Una vez el jugador 1 y el jugador 2 se hayan plantado o se hayan pasado de 21, 
            # si uno de los dos o los dos se pasan de 21 se ejecutará la función se_pasa()
            print(se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)) # Ejecuta la función e imprimirá quien se ha pasado 
            input("PULSA ENTER PARA VER RESULTADOS")
            plantarse_jugador1 = "N"
            plantarse_jugador2 = "N"
            fin = "N"
        plantarse_jugador2 = "N"
        if plantarse_jugador1 == "N" and plantarse_jugador2 == "N":
            fin = "N"
    print(resultado_texto(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)) 
    # Una vez terminada las rondas se llama a la función resultado_texto() y resultado() para imprimir los resultados de la partida
    resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador, nombre, nombre2, tipo_partida)


def resultado_texto(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2):
    """Muestra los resutados finales de las partidas."""
    system("cls")
    jugador1= suma_cartas(cartas_jugador)
    jugador2= suma_cartas(cartas_jugador2)
    if jugador1 <= 21 and jugador2 <= 21: # Mientras los dos jugadores tengan menos de 21 se imprimiran estos resultados
        if jugador1 == jugador2: # Si tienen lo mismo será empate
            return f"JUEGO TERMINADO - Ronda  {str(ronda2)}\n¡Empate!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
        if jugador1 > jugador2: # Si el jugador1 tiene más que el jugador2 gana el jugador1
            return f"JUEGO TERMINADO - Ronda  {str(ronda2)}\n¡Gana J1 - {nombre}!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
        if jugador2 > jugador1: # Si el jugador2 tiene más que el jugador1 gana el jugador2
            return f"JUEGO TERMINADO - Ronda  {str(ronda2)}\n¡Gana J2 - {nombre2}!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
    if jugador1 > 21 or jugador2 > 21: # Si uno de los jugadores o ambos se han pasado de 21 imprimira estos resultados
        if jugador1 > 21 and jugador2 > 21: # Si los dos se pasan de 21 nadie habra ganado
            return f"JUEGO TERMINADO - Ronda  {str(ronda2)}\nGame over ¡Los dos os habéis pasado!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
        elif jugador2 > 21: # Si el jugador2 se pasa gana el jugador1
            return f"JUEGO TERMINADO - Ronda  {str(ronda2)}\n¡Gana J1 - {nombre}!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
        elif jugador1 > 21: # Si el jugador1 se pasa gana el jugador2
            return f"JUEGO TERMINADO - Ronda  {str(ronda2)}\n¡Gana J2 - {nombre2}!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"


def resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador, nombre, nombre2, tipo_partida):
    """Muestra los resutados finales de las partidas."""
    jugador1= suma_cartas(cartas_jugador)
    jugador2= suma_cartas(cartas_jugador2)
    if jugador1 == jugador2:
        jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
    if jugador1 <= 21 and jugador2 <= 21: # Si los dos jugadores tengan menos de 21 se ejecutará esto
        if jugador1 > jugador2: 
            # Si el jugador1 tiene mas que el jugador2 gana el jugador1,
            # se le suma 1 a las rondas ganadas finales y se ejcuta la funcion jugar_de_nuevo()
            rondas_ganadas_jugador1+=1
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
        if jugador2 > jugador1: 
            # Si el jugador2 tiene mas que el jugador1 gana el jugador2,
            # se le suma 1 a las rondas ganadas finales y se ejcuta la funcion jugar_de_nuevo()
            rondas_ganadas_jugador2+=1
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
    if jugador1 > 21 or jugador2 > 21: # Si uno de los jugadores o ambos se han pasado de 21 se ejecutará esto
        if jugador2 > 21: 
            # Si el jugador2 se pasa gana el jugador1
            # se le suma 1 a las rondas ganadas finales y se ejcuta la funcion jugar_de_nuevo()
            rondas_ganadas_jugador1+=1
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
        elif jugador1 > 21: 
            # Si el jugador1 se pasa gana el jugador2,
            # se le suma 1 a las rondas ganadas finales y se ejcuta la funcion jugar_de_nuevo()
            rondas_ganadas_jugador2+=1
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)


def jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2): 
    """Pregunta si quieres volver a jugar, si la respuesta es que si, ejecuta la partida de nuevo, si es que no, llama a la función final_juego."""
    final = 0
    while final == 0:
        quiere_jugar_de_nuevo=input("¿Quieres jugar de nuevo? (S/N) ").upper() # Pregunta si quiere jugar de nuevo
        if quiere_jugar_de_nuevo == "S": # Si responde S se ejecuta
            system("cls")
            if tipo_partida == 1: 
                # Si el tipo de partida que se eligió es el 1 se ejecutará la función jugador1_partida() 
                # y comenzará de nuevo la partida para un solo jugador
                jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)
            if tipo_partida == 2: 
                # Si el tipo de partida que se eligió es el 2 se ejecutará la función jugador2_partida() 
                # y comenzará de nuevo la partida para dos jugadores
                jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)
        elif quiere_jugar_de_nuevo == "N": # Si responde N saldrá del bucle
            final = 1
        else: # Si no se responde ninguna de las dos respuestas anteriores dará un error y volverá a comenzar el bucle
            print("ERROR - INTRODUCE UN DIGITO VALIDO")
    final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2) # Una vez fuera del bucle se llama a al función final_juego()


def modo_de_juego (rondas_ganadas_jugador1,rondas_ganadas_jugador2):
    """Permite elegir entre los dos modos de juegos que tiene, 1 jugador contra la máquina 
        o 2 jugadores o en caso de querer volver al menú poder volver a él"""
    #final = 0
    system("cls")
    print("Eliga el modo de juego al que quiere jugar o vuelva al menú si quiere leer las reglas:\n \n(1) Modo 1 jugador\n(2) Modo 2 jugadores\n(3) Volver al menú")
    jugadores= input("") # Variable jugadores, el usuario teclea cuantos jugadores van a jugar 
    if jugadores == "1":
        # Si se cumple entonces llama a una funcion(nombres()), y se configura la partida para un modo jugador
        tipo_partida= 1
        system("cls")
        print("Partida configurada para 1 jugador y la máquina\n")
        nombres(rondas_ganadas_jugador1,rondas_ganadas_jugador2, tipo_partida) # Llama a la función nombres() para guardar el nombre del jugador 
    elif jugadores == "2":
        # Si se cumple entonces llama a una funcion(nombres()), y se configura la partida para modo dos jugadores
        tipo_partida= 2
        system("cls")
        print("Partida configurada para 2 jugadores\n")
        nombres(rondas_ganadas_jugador1,rondas_ganadas_jugador2, tipo_partida) # Llama a la función nombres() para guardar el nombre de los jugadores
    elif jugadores == "3":
        # Si se cumple entonces llama a una funcion(menu()), para volver al menú
        tipo_partida= 3
        system("cls")
        menu()
    else: # Si se introduce un caracter erróneo da un mensaje de error, y llama a la función modo_de_juego()
        print('**ERROR** - Por favor, introduce solo el numero de las opciones, por ejemplo si quieres la opcion (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')#mejorar el mensaje de error para que tenga sentido algo de elige 1 de un solo jugador o 2 de dos jugadores 
        input()
        modo_de_juego(rondas_ganadas_jugador1,rondas_ganadas_jugador2)


def menu():
    """Menú del blackjack donde se podrá elegir entre ver las reglas del Blackjack o empezar a jugar al Blackjack."""
    rondas_ganadas_jugador1=0
    rondas_ganadas_jugador2=0
    # Borra la pantalla y se imprime por pantalla el menú del blackjack
    system("cls")
    print("Bienvenido a nuestro blackjack.\n¿Qué vas a querer hacer?\nElige una opción:\n(1) Leer las reglas\n(2) Jugar al Blackjack")
    opcion= input()
    if opcion == "1": # Si se cumple entonces llama a una funcion(reglas())
        reglas()
    elif opcion == "2": # Si se cumple entonces llama a una función(modo_de_juego())
        system("cls")
        modo_de_juego(rondas_ganadas_jugador1,rondas_ganadas_jugador2)
    else: # Da un mensaje de error, y empieza de nuevo la función menu()
        print('**ERROR** - Por favor, introduce solo el número de las opciones, por ejemplo si quieres la opción (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')
        input()
        menu()


def main(): # 
    """Es la función principal que desencadena el programa.\n
    Llama a la función menu y comienza el programa"""
    menu()

if __name__=="__main__":
    main()