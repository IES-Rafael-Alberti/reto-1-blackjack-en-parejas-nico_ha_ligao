from blackjat import jugador2_partida
from blackjat import jugador1_partida
from blackjat import final_juego
from blackjat import suma_cartas
from blackjat import pedir_carta
from os import system


#        print("¡Empate!")
#        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
#        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
#    elif jugador > jugador2 and jugador <= 21: #SI jugador <= 21 and jugador > jugador2 or jugador 2 > 21
#        print("¡Gana J1 - jugador1!")
#        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
#        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
#        rondas_ganadas+=1
#    elif jugador <= 21 and jugador > 21: #SI jugador <= 21 and jugador > jugador2 or jugador 2 > 21
#        print("¡Gana J1 - jugador1!")
#        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
#        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
#        rondas_ganadas+=1
#    elif jugador < jugador2 and jugador2 <= 21:
#        print("¡Gana J2 - jugador2!")
#        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
#        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")") 
#    else:
#        print("JUEGO TERMINADO\nGame over ¡Los dos os habéis pasado!")
#        print("tus cartas "+nombre1+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
#        print("las cartas "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
#
#
#
#------------------------------FUNCION RESULTADO FALTA RETURN SI NECESITA---------------------------------------------------------------------
#def resultado():
#    # Una vez terminada la partida se 
#    #jugador1 = 24
#    #jugador2 = 24
#    #nombre1 = "pepe"
#    #nombre2 = "antonio"
#    #cartas_jugador = "567"
#    #cartas_jugador2 = "568"
#    #suma_cartas = 24
#    #suma_cartas2 = 24
#    system("cls")
#    jugador1= suma_cartas(cartas_jugador)
#    jugador2= suma_cartas(cartas_jugador2)
#    if jugador1 <= 21 and jugador2 <= 21:
#        if jugador1 == jugador2:
#            print("¡Empate!")
#            print(f"J1 - {nombre1} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
#            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
#        if jugador1 > jugador2:
#            print("¡Gana J1 - jugador1!")
#            print(f"J1 - {nombre1} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
#            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
#        if jugador2 > jugador1:
#            print("¡Gana J2 - jugador2!")
#            print(f"J1 - {nombre1} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
#            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas2(cartas_jugador2))})")
#    if jugador1 > 21 or jugador2 > 21:
#        if jugador1 > 21 and jugador2 > 21:
#            print("JUEGO TERMINADO\nGame over ¡Los dos os habéis pasado!")
#            print(f"J1 - {nombre1} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
#            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
#        elif jugador2 > 21:
#            print("¡Gana J1 - jugador1!")
#            print(f"J1 - {nombre1} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
#            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")
#        elif jugador1 > 21:
#            print("¡Gana J2 - jugador2!")
#            print(f"J1 - {nombre1} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})")
#            print(f"J2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})")

#-------------------------------------------------------------------------------------------------------

#------------------------------FUCION JUGAR DE NUEVO FALTA RETURN----------------------------------------------------------------------------------
#def jugar_de_nuevo1():
#    final = 0
#    while final == 0:
#        quiere_jugar_de_nuevo=input("¿quieres jugar de nuevo? (S/N)")
#        if quiere_jugar_de_nuevo == "S":
#            jugador1_partida(5)
#        if quiere_jugar_de_nuevo == "N":
#            final = 1
#            final_juego(5)
#        else:
#            print("ERROR - INTRODUCE UN DIGITO VALIDO")
#def jugar_de_nuevo2():
#    final = 0
#    while final == 0:
#        quiere_jugar_de_nuevo=input("¿quieres jugar de nuevo? (S/N)")
#        if quiere_jugar_de_nuevo == "S":
#            jugador2_partida(5)
#        if quiere_jugar_de_nuevo == "N":
#            final = 1
#            final_juego(5)
#        else:
#            print("ERROR - INTRODUCE UN DIGITO VALIDO")

#-----------------------------------------------------------------------------------------------



def ronda_1():
    rondas = 1
    ronda = f"RONDA {rondas}"
    while len(cartas_jugador) < 2:
        system("cls")
        print(ronda)
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
    rondas += 1
    print(ronda)
    print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
    return rondas

def rondas_2(rondas):
    system("cls")
    print("tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    print("las cartas de la maquina son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
    while plantarse == "S" and suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_maquina)<22:
        system("cls")
        rondas += 1
        print(f"RONDA {rondas}")
        print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?")
        if pedir == "S":
            cartas_jugador+=pedir_carta()
        print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        if suma_cartas(cartas_maquina) <= 16:
            cartas_maquina+=pedir_carta()
        if pedir=="N":
            plantarse="N"

rondas = ronda_1()
rondas_2(rondas)