import random
def pedir_carta(): #esta funcion coge un valor aleatorio con random y devuelve una letra de la cadena baraja
    baraja = "A234567890JKQ"
    numero =random.randint(0,12)
    carta = baraja[numero]
    return carta
def cartas_iniciales():#esta funcion da las dos cartas del principio ya tienes un turno hecho el obligatorio, asi que puedes dar al usuario la opcion de plantarse automaticamente
    cartas=""
    for i in range(1,3):
        cartas+= str(pedir_carta())
    return cartas
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
        else:
            suma_carta+=int(una_carta)
        contador+=1
    if suma_carta > 21:
        if "A" in cartas:
            suma_carta-=-9
    return suma_carta
def jugador1_partida(rondas_ganadas):#son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    cartas_jugador = ""
    suma_carta_jugador = 0
    cartas_maquina = ""
    suma_cartas_maquina= 0
    salir= "S"
    cartas_jugador+=cartas_iniciales()
    print("las cartas del jugador son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    cartas_maquina+=cartas_iniciales()
    print("las cartas del jugador son: "+cartas_maquina+"("+str(suma_cartas(cartas_maquina))+")")
