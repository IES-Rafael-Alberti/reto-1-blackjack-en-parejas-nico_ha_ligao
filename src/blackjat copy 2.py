from os import system
import random
def reglas():#esta funcion imprime por pantalla las reglas del blackjat
    print("Objetivo del juego:\n\n- Conseguir 21 puntos o plantarse con más puntos que el otro jugador.")
    print("- Si el jugador se pasa de 21, pierde automáticamente.")
    print("- Si nadie se pasa, gana el jugador con la mano más cercana a 21.")
    print("- Conseguir 21 puntos o plantarse con más puntos que el otro jugador.")
    print("- Las cartas numéricas valen su número, las figuras valen 10 y el As puede valer 1 u 10.\n")
    print("- Pulsa enter para volver al menu.")
    input()
    system("cls")
    menu()


def nombres(rondas_ganadas_jugador1,rondas_ganadas_jugador2, tipo_partida):
    if tipo_partida == 1:
        nombre=input("¿Quién va a ser el jugador? ")
        nombre2= "maquina"
        jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)
    if tipo_partida == 2:
        nombre=input("¿Quién va a ser el jugador 1? ")
        nombre2=input("¿Quién va a ser el jugador 2? ")
        jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)


def pedir_carta(): #esta funcion coge un valor aleatorio con random y devuelve una letra de la cadena baraja
    baraja = "A234567890JKQ"
    numero =random.randint(0,12)
    carta = baraja[numero]
    return carta


def suma_cartas(cartas):#esta funcion despedaza las cartas del jugador y las suma una a nua y te devuelve las sumas de las cartas
    contador= 0
    suma_carta=0
    for i in range (1,(len(cartas)+1)):
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
        else:
            suma_carta+=int(una_carta)
        contador+=1
    if suma_carta > 21:
        if "A" in cartas:
            suma_carta-=9
    return suma_carta

def final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2):
    system("cls")
    print("el jugador "+ nombre+" ganado un total de: " + str(rondas_ganadas_jugador1)+ " rondas") #ESTA MAL HAY QUE ARREGLAR
    print("el jugador "+ nombre2+" ganado un total de: " + str(rondas_ganadas_jugador2)+ " rondas") #ESTA MAL HAY QUE ARREGLAR
    print("Gracias por jugar a nuestro Blackjack.")
    print("Trabajo desarrollado por Nicolas De Gomar Almellones e Iván López Jiménez")
    while_menu=0
    while while_menu == 0:
        volver_menu=input("¿Quieres volver al menu?(S/N)")
        if volver_menu == "S":
            system("cls")
            menu()
            while_menu = 1
        elif volver_menu== "N":
            system("cls")
            print("Programa finalizado, dale enter para cerrar la ventana")
            while_menu = 1
        else:
            print("ERROR - INTRODUCE UN DIGITO VALIDO")
    input()
    system("cls")
    

def jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida):#son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    pedir = ""
    ronda2 = 0
    plantarse="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    cartas_jugador+=pedir_carta()
    cartas_jugador2+=pedir_carta()
    system("cls")

    while len(cartas_jugador) < 2:
        system("cls")
        ronda2 = ronda1(ronda2)
        print(f"RONDA {ronda2}")
        print(nombre +" tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la "+ nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
            cartas_jugador2+=pedir_carta()
        else:
            print("ERROR EN EL PRIMER TURNO DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()

    while plantarse == "S" and suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_jugador2)<22:
        system("cls")
        ronda2 = ronda1(ronda2)
        print(f"RONDA {ronda2}")
        print(nombre +"tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
        print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        if suma_cartas(cartas_jugador2) <= 16:
            cartas_jugador2+=pedir_carta()
        if pedir=="N":
            plantarse="N"
    se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)
    resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2,tipo_partida)



def se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2): # OKEY
    system("cls")
    if suma_cartas(cartas_jugador2) > 21:
        print("RONDA " + str(ronda2))
        print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
        print(f"J2 - {nombre2} - {cartas_jugador2} **se pasa**")
        input("PULSA ENTER PARA VER RESULTADOS")
    elif suma_cartas(cartas_jugador) > 21:
        print("RONDA " + str(ronda2))
        print(f"J1 - {nombre} - {cartas_jugador} **se pasa**")
        print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
        input("PULSA ENTER PARA VER RESULTADOS")

def ronda1(ronda2): # OKEY
    ronda2 += 1
    return ronda2

# ARREGLAR RONDAS DE PARTIDA DE DOS JUGADORES

def jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida):#son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    pedir = ""
    ronda2 = 0
    plantarse_jugador1="S"
    plantarse_jugador2="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    cartas_jugador+=pedir_carta()
    print("las cartas del "+nombre+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    cartas_jugador2+=pedir_carta()
    print("las cartas del "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    input("ENTER PARA EMPEZAR")
    system("cls")
    while len(cartas_jugador) < 2:
        system("cls")
        ronda2 = ronda1(ronda2)
        print(f"RONDA {ronda2}")
        print("tus carta "+nombre+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
        else:
            print("ERROR EN EL PRIMER TURNO "+ nombre +  "DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    while len(cartas_jugador2) < 2:
        system("cls")
        print(f"RONDA {ronda2}")
        print("tus carta "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador2+=pedir_carta()
        else:
            print("ERROR EN EL PRIMER TURNO "+ nombre2 +  " DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    system("cls")
    print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    print("las cartas de la maquina son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    fin = "S"
    while fin == "S" and suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_jugador)<22:
        ronda2 = ronda1(ronda2)
        while plantarse_jugador1 == "S" and suma_cartas(cartas_jugador)<22:
            system("cls")
            print(f"RONDA {ronda2}")
            print("tus cartas "+ nombre +  " son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
            if pedir == "S":
                cartas_jugador+=pedir_carta()
            # print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            if pedir=="N":
                plantarse_jugador1="N"
        se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)
        while plantarse_jugador2 == "S" and suma_cartas(cartas_jugador2)<22:
            system("cls")
            print(f"RONDA {ronda2}")
            print("tus cartas"+ nombre2 +  " son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
            pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
            if pedir == "S":
                cartas_jugador2+=pedir_carta()
            # print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            if pedir=="N":
                plantarse_jugador2="N"
        se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)
        plantarse_jugador2 = "N"
        if plantarse_jugador1 == "N" and plantarse_jugador2 == "N":
            fin = "N"
    resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)
    jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida)



def resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2, tipo_partida):
    system("cls")
    jugador1= suma_cartas(cartas_jugador)
    jugador2= suma_cartas(cartas_jugador2)
    if jugador1 <= 21 and jugador2 <= 21: # mientras los dos jugadores tengan menos de 21 se imprimiran estos resultados
        if jugador1 == jugador2: # si tienen lo mismo sera empate
            print("JUEGO TERMINADO - Ronda " + str(ronda2) + "\n¡Empate!")
            print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
        if jugador1 > jugador2: #Si el jugador1 tiene mas que el jugador2 gana el jugador1
            print("JUEGO TERMINADO - Ronda " + str(ronda2) + "¡Gana J1 - jugador1!")
            rondas_ganadas_jugador1+=1
            print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
        if jugador2 > jugador1: #Si el jugador2 tiene mas que el jugador1 gana el jugador2
            print("JUEGO TERMINADO - Ronda " + str(ronda2) + "¡Gana J2 - jugador2!")
            rondas_ganadas_jugador2+=1
            print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
    if jugador1 > 21 or jugador2 > 21: #Si uno de los jugadores o ambos se han pasado de 21 imprimira estos resultados
        if jugador1 > 21 and jugador2 > 21: #si los dos se pasan de 21 nadie habra ganado
            print("JUEGO TERMINADO\nGame over ¡Los dos os habéis pasado!")
            print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
        elif jugador2 > 21: #si el jugador2 se pasa gana el jugador1
            print("JUEGO TERMINADO - Ronda " + str(ronda2) + "¡Gana J1 - jugador1!")
            rondas_ganadas_jugador1+=1
            print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)
        elif jugador1 > 21: #si el jugador1 se pasa gana el jugador2
            print("JUEGO TERMINADO - Ronda " + str(ronda2) + "¡Gana J2 - jugador2!")
            rondas_ganadas_jugador2+=1
            print(f"J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
            jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2)

def jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2): #este bucle sirve para preguntar si se quiere jugar de nuevo y en caso de que sea S empezara las partidas de nuevo y en caso de que se N terminara el programa y se ejecutara la funcion final_juego
    final = 0
    while final == 0:
        quiere_jugar_de_nuevo=input("¿quieres jugar de nuevo? (S/N)")
        if quiere_jugar_de_nuevo == "S":
            system("cls")
            if tipo_partida == 1:
                jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)
            if tipo_partida == 2:
                jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida)
        elif quiere_jugar_de_nuevo == "N":
            final = 1
        else:
            print("ERROR - INTRODUCE UN DIGITO VALIDO")
    final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2)





def modo_de_juego (rondas_ganadas_jugador1,rondas_ganadas_jugador2):#esta funcion elige entre jugar un jugador o dos jugadores
    rondas=0
    system("cls")
    print("¿cuantos jugadores vais a hacer?(1/2)")
    jugadores= input() #variable jugadores, el usuario teclea el usuario teclea cuantos jugadores son 
    if jugadores == "1":#si se cumple entonces llama a una funcion(jugador1_menu()), y se configura la partida para este modo 
        tipo_partida= 1
        system("cls")
        print("Partida configurada para 1 jugador y la maquina")
        nombres(rondas_ganadas_jugador1,rondas_ganadas_jugador2, tipo_partida)
        #jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2)
    elif jugadores == "2":#si se cumple entonces llama a una funcion(jugador2_menu()), y se configura la partida para este modo 
        tipo_partida= 2
        system("cls")
        print("Partida configurada para 2 jugadores")
        nombres(rondas_ganadas_jugador1,rondas_ganadas_jugador2, tipo_partida)
        #jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2)
    else:#da un mensaje de error, y empieza de nuevo la funcion correspondiente
        print('ERROR - Por favor, introduce solo el numero de las opciones, por ejemplo si quieres la opcion (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')#mejorar el mensaje de error para que tenga sentido algo de elige 1 de un solo jugador o 2 de dos jugadores 
        input()
        modo_de_juego()


def menu():#esta funcion lo que hace es que tienes un pequeño menu donde poder elegir varias opciones en este caso puede elegir leer reglas o jugar partida
    rondas_ganadas_jugador1=0
    rondas_ganadas_jugador2=0
    system("cls")
    print("Bienvenido al blackjat.\n¿Que vas a querer hacer?\nElige una opcion:\n(1) Leer las reglas\n(2) Jugar al blackjat")
    opcion= input() #variable jugadores, el usuario teclea el usuario teclea cuantos jugadores son 
    if opcion == "1":#si se cumple entonces llama a una funcion(jugador1_menu()), y se configura la partida para este modo 
        reglas()
    elif opcion == "2":#si se cumple entonces llama a una funcion(modo_de_juego()), y se abre una pantalla donde eliges los jugadores 
        system("cls")
        modo_de_juego(rondas_ganadas_jugador1,rondas_ganadas_jugador2)
    else:#da un mensaje de error, y empieza de nuevo la funcion correspondiente
        print('ERROR - Por favor, introduce solo el numero de las opciones, por ejemplo si quieres la opcion (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')
        input()
        menu()


def main():
    menu()

if __name__=="__main__":
    main()

#tenemos que ver si mejorar todo, explotar mas el programa y demas ver si hay fallos que podemos corregir, el programa esta muy avanzado, para lo que llevamos, mejorar faltas de ortografia, mejorar frases, mejorar documentacion, mañana lo vemos todo, saludos 
#tenemos que meter las pruebas unitarias 
#mejorar algunos modulos 

# MIRAR FUNCIONES DE LAS PARTIDAS PARA VER SI SE PUEDEN METER EN UNA FUNCION O NO
# TERMINAR DE DOCUMENTAR
# REALIZAR PYTEST DE MAS FUNCIONES
# QUITAR CODIGO COMETADO SI NO SE VA A UTILIZAR


#pruebas unitarias de todo lo que no tenga inputs :D
#jugador 1 no suma funciones rondas