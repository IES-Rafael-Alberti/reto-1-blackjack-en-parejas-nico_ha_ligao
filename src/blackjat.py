from os import system
import random
def reglas():#esta funcion imprime por pantalla las reglas del blackjat
    print("Objetivo del juego:\nConseguir 21 puntos o plantarse con más puntos que el otro jugador.\n")
    print("Pulsa enter para volver al menu.")
    input()
    system("cls")
    menu()


def pedir_carta(): #esta funcion coge un valor aleatorio con random y devuelve una letra de la cadena baraja
    baraja = "A234567890JKQ"
    numero =random.randint(0,12)
    carta = baraja[numero]
    return carta


def suma_cartas(cartas):#esta funcion despedaza las cartas del jjugador y las suma una a nua y te devuelve las sumas de las cartas
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
            suma_carta-=-9
    return suma_carta

def final_juego(rondas_ganadas):
    system("cls")
    print("Has ganado un total de: " + str(rondas_ganadas)+ "rondas")
    print("Trabajo desarrollado por Nicolas De Gomar Almellones e Ivan Lopez Jimenez")

def jugador1_partida(rondas_ganadas):#son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    quiere_jugar_de_nuevo=""
    pedir = ""
    plantarse="S"
    cartas_jugador = ""
    cartas_maquina = ""
    cartas_jugador+=pedir_carta()
    print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    cartas_maquina+=pedir_carta()
    print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
    system("cls")
    while len(cartas_jugador) < 2:
        system("cls")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
            cartas_maquina+=pedir_carta()
        else:
            print("ERROR EN EL PRIMER TURNO DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    system("cls")
    print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
    while plantarse == "S" and suma_cartas(cartas_jugador)<22:
        system("cls")
        print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
        print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        if suma_cartas(cartas_maquina) <16:
            cartas_maquina+=pedir_carta()
        if pedir=="N":
            plantarse="N"
    system("cls")
    jugador= suma_cartas(cartas_jugador)
    jugador2= suma_cartas(cartas_maquina)
    if jugador == jugador2 and jugador > 22 and jugador2 > 22:
        print("¡Empate!")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
    elif jugador > jugador2 and jugador <= 21:
        print("¡Gana J1 - jugador1!")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")") 
        rondas_ganadas+=1
    elif jugador < jugador2 and jugador <= 21:
        print("¡Gana J1 - jugador1!")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")") 
        rondas_ganadas+=1
    elif jugador < jugador2 and jugador2 <= 21:
        print("¡Gana J2 - jugador2!")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")") 
    elif jugador > jugador2 and jugador2 <= 21:
        print("¡Gana J2 - jugador2!")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")") 
    else:
        print("JUEGO TERMINADO\nGame over ¡Los dos os habéis pasado!")
        print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")") 
    final = 0
    while final == 0:
        quiere_jugar_de_nuevo=input("¿quieres jugar de nuevo? (S/N)")
        if quiere_jugar_de_nuevo == "S":
            jugador1_partida(rondas_ganadas)
        if quiere_jugar_de_nuevo == "N":
            final = 1
            final_juego(rondas_ganadas)
        else:
            print("ERROR - INTRODUCE UN DIGITO VALIDO")




def jugador2_partida(rondas_ganadas):#son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    nombre1=input("¿quien va a ser el jugador 1?")
    nombre2=input("¿quien va a ser el jugador 2?")
    quiere_jugar_de_nuevo=""
    pedir = ""
    plantarse_jugador1="S"
    plantarse_jugador2="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    cartas_jugador+=pedir_carta()
    print("las cartas del "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    cartas_jugador2+=pedir_carta()
    print("las cartas del "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    input("ENTER PARA EMPEZAR")
    system("cls")
    
    while len(cartas_jugador) < 2:
        system("cls")
        print("tus carta "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
        else:
            print("ERROR EN EL PRIMER TURNO "+ nombre1 +  "DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    while len(cartas_jugador2) < 2:
        system("cls")
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
    while suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_jugador)<22:
        while plantarse_jugador1 == "S" and suma_cartas(cartas_jugador)<22:
            system("cls")
            print("tus cartas"+ nombre1 +  " son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
            if pedir == "S":
                cartas_jugador+=pedir_carta()
            print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            if pedir=="N":
                plantarse_jugador1="N"
        while plantarse_jugador2 == "S" and suma_cartas(cartas_jugador)<22:
            system("cls")
            print("tus cartas"+ nombre2 +  " son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
            if pedir == "S":
                cartas_jugador+=pedir_carta()
            print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
            if pedir=="N":
                plantarse_jugador2="N"
    system("cls")
    jugador= suma_cartas(cartas_jugador)
    jugador2= suma_cartas(cartas_jugador2)
    if jugador == jugador2 and jugador > 22 and jugador2 > 22:
        print("¡Empate!")
        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    elif jugador > jugador2 and jugador <= 21:
        print("¡Gana J1 - jugador1!")
        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
        rondas_ganadas+=1
    elif jugador < jugador2 and jugador <= 21:
        print("¡Gana J1 - jugador1!")
        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
        rondas_ganadas+=1
    elif jugador < jugador2 and jugador2 <= 21:
        print("¡Gana J2 - jugador2!")
        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    elif jugador > jugador2 and jugador2 <= 21:
        print("¡Gana J2 - jugador2!")
        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")") 
    else:
        print("JUEGO TERMINADO\nGame over ¡Los dos os habéis pasado!")
        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    final = 0
    while final == 0:
        quiere_jugar_de_nuevo=input("¿quieres jugar de nuevo? (S/N)")
        if quiere_jugar_de_nuevo == "S":
            jugador2_partida(rondas_ganadas)
        if quiere_jugar_de_nuevo == "N":
            final = 1
            final_juego(rondas_ganadas)
        else:
            print("ERROR - INTRODUCE UN DIGITO VALIDO")


def modo_de_juego ():#esta funcion elige entre jugar un jugador o dos jugadores
    rondas=0
    system("cls")
    print("¿cuantos jugadores vais a hacer?(1/2)")
    jugadores= input() #variable jugadores, el usuario teclea el usuario teclea cuantos jugadores son 
    if jugadores == "1":#si se cumple entonces llama a una funcion(jugador1_menu()), y se configura la partida para este modo 
        system("cls")
        print("Partida configurada para 1 jugador y la maquina")
        jugador1_partida(rondas)
    elif jugadores == "2":#si se cumple entonces llama a una funcion(jugador2_menu()), y se configura la partida para este modo 
        system("cls")
        print("Partida configurada para 2 jugadores")
        jugador2_partida(rondas)
    else:#da un mensaje de error, y empieza de nuevo la funcion correspondiente
        print('ERROR - Por favor, introduce solo el numero de las opciones, por ejemplo si quieres la opcion (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')#mejorar el mensaje de error para que tenga sentido algo de elige 1 de un solo jugador o 2 de dos jugadores 
        input()
        modo_de_juego()


def menu():#esta funcion lo que hace es que tienes un pequeño menu donde poder elegir varias opciones en este caso puede elegir leer reglas o jugar partida
    system("cls")
    print("Bienvenido al blackjat.\n¿Que vas a querer hacer?\nElige una opcion:\n(1) Leer las reglas\n(2) Jugar al blackjat")
    opcion= input() #variable jugadores, el usuario teclea el usuario teclea cuantos jugadores son 
    if opcion == "1":#si se cumple entonces llama a una funcion(jugador1_menu()), y se configura la partida para este modo 
        reglas()
    elif opcion == "2":#si se cumple entonces llama a una funcion(modo_de_juego()), y se abre una pantalla donde eliges los jugadores 
        system("cls")
        modo_de_juego()
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

#pruebas unitarias de todo lo que no tenga inputs :D