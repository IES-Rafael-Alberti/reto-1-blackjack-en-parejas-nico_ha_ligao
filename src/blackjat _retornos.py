from os import system
import random
def reglas():
    """Esta funcion imprime por pantalla las reglas del blackjat."""
    system("cls")
    print("Objetivo del juego:\n\n- Conseguir 21 puntos o plantarse con más puntos que el otro jugador.")
    print("- Si el jugador se pasa de 21, pierde automáticamente.")
    print("- Si nadie se pasa, gana el jugador con la mano más cercana a 21.")
    print("- Conseguir 21 puntos o plantarse con más puntos que el otro jugador.")
    print("- Las cartas numéricas valen su número, las figuras valen 10 y el As puede valer 1 u 10.\n")
    print("- Pulsa enter para volver al menu.")
    input()
    system("cls")

def nombres(tipo_partida):
    """Pide los nombres de los jugadores que van a jugar cada partida y comienza la partida."""
    if tipo_partida == "1 jugador": # Si la partida es del modo un jugador preguntará el nombre del jugador y comenzará la partida
        nombre=input("¿Quién va a ser el jugador? ")
        return nombre
    if tipo_partida == "2 jugadores": # Si la partida es del modo dos jugadores preguntará el nombre de los jugadores y comenzará la partida
        nombre=input("¿Quién va a ser el jugador 1? ")
        return nombre

def nombres2(tipo_partida):
    """Pide los nombres de los jugadores que van a jugar cada partida y comienza la partida."""
    if tipo_partida == "1 jugador": # Si la partida es del modo un jugador preguntará el nombre del jugador y comenzará la partida
        nombre2= "maquina"
        return nombre2
    if tipo_partida == "2 jugadores": # Si la partida es del modo dos jugadores preguntará el nombre de los jugadores y comenzará la partida
        nombre2=input("¿Quién va a ser el jugador 2? ")
        return nombre2

def numero_aleatorio():
    numero=random.randint(0,12)
    return numero

def pedir_carta(numero):
    """Da valor aleatorio entre las cartas que hay con random y devuelve una letra de la cadena baraja."""
    baraja = "A234567890JKQ"
    carta = baraja[numero] # Carta corresponde a un caracter aleatorio de las posiciones 0 y 12 de baraja 
    return carta

def suma_cartas(cartas):
    """Comprueba las cartas del jugador y las suma una a una y te devuelve las sumas de las cartas."""
    contador= 0
    suma_carta=0
    for i in range (1,(len(cartas)+1)): # El bucle se ejecutara carta por carta que tenga en la mano, si en la mano del jugador hay una A, J, K, Q, o 0 le dará el valor de 10 a la suma
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

def final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2,final):
    """Imprime las rondas que han ganado los jugadores y pregunra si se quiere volver al menú, si es que si, vuelve al menú inicial, y si es que no, el programa finaliza."""
    system("cls")
    print("el jugador "+ nombre+" ganado un total de: " + str(rondas_ganadas_jugador1)+ " rondas")
    print("el jugador "+ nombre2+" ganado un total de: " + str(rondas_ganadas_jugador2)+ " rondas")
    print("Gracias por jugar a nuestro Blackjack.")
    print("Trabajo desarrollado por Nicolas De Gomar Almellones e Iván López Jiménez")
    while_menu=0
    while while_menu == 0:
        volver_menu=input("¿Quieres volver al menu?(S/N)").upper() # Pide al jugador si quiere volver al menu
        if volver_menu == "S": # Si escribe S se ejecutará la función menu()
            system("cls")
            menu()
            while_menu = 1
        elif volver_menu== "N": # Si escribe N, el programa finalizará 
            system("cls")
            print("Programa finalizado, dale enter para cerrar la ventana")
            while_menu = 1
        else:
            print("ERROR - INTRODUCE UN DIGITO VALIDO")
    input()
    system("cls")
    exit()

def jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida,final):#son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    pedir = ""
    ronda2 = 0
    plantarse="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    numero = numero_aleatorio()
    cartas_jugador+=pedir_carta(numero) # Se le da un a carta al jugador 1
    numero = numero_aleatorio()
    cartas_jugador2+=pedir_carta(numero) # Se le da un a carta a la máquina
    system("cls")
    while len(cartas_jugador) < 2: # Mientras el jugador 1 solo tenga un carta se ejecutara el bucle
        system("cls")
        ronda2 = ronda1(ronda2) # Llama a la función ronda1()
        print(f"RONDA {ronda2}")
        print(nombre +" tus carta son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        print("las cartas de la "+ nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?").upper() # Pregunta si quiere una carta o no, en este caso el jugador debe pedir una carta obligatoriamente por lo que si no lo hace da un error.
        if pedir == "S": # Si el jugador pide una carta se le dará una carta más y saldrá del bucle
            numero = numero_aleatorio()
            cartas_jugador+=pedir_carta(numero)
            numero = numero_aleatorio()
            cartas_jugador2+=pedir_carta(numero)
        else: # Si el jugador no pide una carta dará error y empezará de nuevo el bucle
            print("ERROR EN EL PRIMER TURNO DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    while plantarse == "S" and suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_jugador2)<22:  # Una vez terminada la primera ronda donde se debe pedir obligatoriamente se borra la pantalla y entra en un bucle donde se jugarán las demás rondas hasta que el jugador se plante o el jugador o la máquina se pasen de 21
        system("cls")
        ronda2 = ronda1(ronda2)
        print(f"RONDA {ronda2}")
        print(nombre +"tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?").upper() # Pregunta si quiere una carta o no, al no ser obligatoria pedir otra carta más podra elegir entre pedir otra carta o plantarse
        if pedir == "S":
            numero = numero_aleatorio()
            cartas_jugador+=pedir_carta(numero)
        print("tus cartas son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        if suma_cartas(cartas_jugador2) <= 16:
            numero = numero_aleatorio()
            cartas_jugador2+=pedir_carta(numero)
        if pedir=="N":
            plantarse="N"
    return rondas_ganadas_jugador1,rondas_ganadas_jugador2,cartas_jugador,cartas_jugador2,ronda2

def se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2):
    """Comprueba si alguno de los jugadores de la partida se ha pasado de 21 y si es correcto imprime el jugador que se ha pasado."""
    system("cls")
    if suma_cartas(cartas_jugador2) > 21: # Si el jugador 2 se ha pasado de 21 se imprime que se ha pasado
        return f"RONDA {str(ronda2)}\n J1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\n J2 - {nombre2} - {cartas_jugador2} **se pasa**"
    elif suma_cartas(cartas_jugador) > 21: # Si el jugador 1 se ha pasado de 21 se imprime que se ha pasado
        return "RONDA " + str(ronda2)+ "\n J1 - "+nombre+" - "+cartas_jugador+" **se pasa**\n J2 - "+nombre2+" - "+cartas_jugador2 + (str(suma_cartas(cartas_jugador2)))    

def ronda1(ronda2): 
    """Suma las rondas que se van jugando."""
    ronda2 += 1
    return ronda2

def jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida,final):# Son los pseudosmain, es donde se guardaran todas las variables de los jugadores, partidas y estadisticas
    """Ejecuta la partida para dos jugadores hasta que no se quiera jugar más."""
    pedir = ""
    pedir2 = ""
    ronda2 = 0
    plantarse_jugador1="S"
    plantarse_jugador2="S"
    cartas_jugador = ""
    cartas_jugador2 = ""
    numero = numero_aleatorio()
    cartas_jugador+=pedir_carta(numero) # Se le da un a carta al jugador 1
    system("cls")
    ronda2 = ronda1(ronda2) # Llama a la función ronda1()
    print(f"RONDA {ronda2}")
    print("las cartas del "+nombre+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
    numero = numero_aleatorio()
    cartas_jugador2+=pedir_carta(numero) # Se le da un a carta al jugador 2
    print("las cartas del "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
    input("ENTER PARA EMPEZAR")
    system("cls")
    while len(cartas_jugador) < 2: # Mientras el jugador 1 solo tenga un carta se ejecutara el bucle
        system("cls")
        print(f"RONDA {ronda2}")
        print("tus carta "+nombre+" son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
        pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?").upper() # Pregunta si quiere una carta o no, en este caso el jugador debe pedir una carta obligatoriamente por lo que si no lo hace da un error.
        if pedir == "S": # Si el jugador pide una carta se le dará una carta más y saldrá del bucle
            numero = numero_aleatorio()
            cartas_jugador+=pedir_carta(numero)
        else: # Si el jugador no pide una carta dará error y empezará de nuevo el bucle
            print("ERROR EN EL PRIMER TURNO "+ nombre +  "DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    while len(cartas_jugador2) < 2: # Mientras el jugador 2 solo tenga un carta se ejecutara el bucle
        system("cls")
        print(f"RONDA {ronda2}")
        print("tus carta "+nombre2+" son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
        pedir2=input("¿quieres pedir una carta mas(S) o plantarte(N)?").upper() # Pregunta si quiere una carta o no, en este caso el jugador debe pedir una carta obligatoriamente por lo que si no lo hace da un error.
        if pedir2 == "S": # Si el jugador pide una carta se le dará una carta más y saldrá del bucle
            numero = numero_aleatorio()
            cartas_jugador2+=pedir_carta(numero)
        else: # Si el jugador no pide una carta dará error y empezará de nuevo el bucle
            print("ERROR EN EL PRIMER TURNO "+ nombre2 +  " DEBES DE PEDIR UNA CARTA \n PULSA ENTER PARA EMPEZAR DE NUEVO")
            input()
    system("cls") 
    fin = "S"
    while fin == "S" and suma_cartas(cartas_jugador)<22 and suma_cartas(cartas_jugador)<22: # Una vez terminada la primera ronda donde se debe pedir obligatoriamente se borra la pantalla y entra en un bucle donde se jugarán las demás rondas hasta que los dos jugadores se planten o uno de los dos se pase de 21
        while (plantarse_jugador1 == "S" and suma_cartas(cartas_jugador)<22) or (plantarse_jugador2 == "S"  and suma_cartas(cartas_jugador2)<22):
            ronda2 = ronda1(ronda2)
            if plantarse_jugador1 == "S" and suma_cartas(cartas_jugador)<22:
                system("cls")
                print(f"RONDA {ronda2}")
                print("tus cartas "+ nombre +  " son: "+cartas_jugador+"("+str(suma_cartas(cartas_jugador))+")")
                pedir=input("¿quieres pedir una carta mas(S) o plantarte(N)?").upper()
                if pedir == "S":
                    numero = numero_aleatorio()
                    cartas_jugador+=pedir_carta(numero)
                if pedir=="N":
                    plantarse_jugador1="N"
            if suma_cartas(cartas_jugador)>21 or suma_cartas(cartas_jugador2)>21: # Si la suma de las cartas de uno de los jugadores es mayor a 21 se ejecuta la función se_pasa y sale del bucle
                ronda2 = ronda1(ronda2)
                se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2) # Comrpueba si las cartas de los jugadores se pasan de 21 y si es así imprime el jugador que se ha pasado
                plantarse_jugador1 = "N"
                plantarse_jugador2 = "N"
                fin = "N"
            if plantarse_jugador2 == "S" and suma_cartas(cartas_jugador2)<22:
                system("cls")
                print(f"RONDA {ronda2}")
                print("tus cartas "+ nombre2 +  " son: "+cartas_jugador2+"("+str(suma_cartas(cartas_jugador2))+")")
                pedir2=input("¿quieres pedir una carta mas(S) o plantarte(N)?").upper()
                if pedir2 == "S":
                    numero = numero_aleatorio()
                    cartas_jugador2+=pedir_carta(numero)
                if pedir2=="N":
                    plantarse_jugador2="N"
                if suma_cartas(cartas_jugador2)>21 or suma_cartas(cartas_jugador)>21:# Si la suma de las cartas de uno de los jugadores es mayor a 21 se ejecuta la función se_pasa y sale del bucle
                    ronda2 = ronda1(ronda2)
                    se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2) # Comrpueba si las cartas de los jugadores se pasan de 21 y si es así imprime el jugador que se ha pasado
                    plantarse_jugador1 = "N"
                    plantarse_jugador2 = "N"
                    fin = "N"
        plantarse_jugador2 = "N"
        if plantarse_jugador1 == "N" and plantarse_jugador2 == "N":
            fin = "N"
    resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2, tipo_partida,final) # Una vez terminada el bucle de las rondas se llama a la función resultados para imprimir los resultados de la partida

def resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2, tipo_partida,final):
    """Muestra los resutados finales de las partidas."""
    system("cls")
    jugador1= suma_cartas(cartas_jugador)
    jugador2= suma_cartas(cartas_jugador2)
    if jugador1 <= 21 and jugador2 <= 21: # Mientras los dos jugadores tengan menos de 21 se imprimiran estos resultados
        if jugador1 == jugador2: # Si tienen lo mismo sera empate
            return f"JUEGO TERMINADO - Ronda {ronda2}\n ¡Empate!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))}\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))}))"
        if jugador1 > jugador2: # Si el jugador1 tiene mas que el jugador2 gana el jugador1
            rondas_ganadas_jugador1+=1
            return f"JUEGO TERMINADO - Ronda {ronda2}\n¡Gana J1 - jugador1!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
        if jugador2 > jugador1: # Si el jugador2 tiene mas que el jugador1 gana el jugador2
            rondas_ganadas_jugador2+=1
            return f"JUEGO TERMINADO - Ronda {ronda2}\n¡Gana J2 - jugador2!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
    if jugador1 > 21 or jugador2 > 21: # Si uno de los jugadores o ambos se han pasado de 21 imprimira estos resultados
        #if jugador1 > 21 and jugador2 > 21: # Si los dos se pasan de 21 nadie habra ganado
        #    return f"JUEGO TERMINADO\nGame over ¡Los dos os habéis pasado!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})"
        if jugador2 > 21: # Si el jugador2 se pasa gana el jugador1
            rondas_ganadas_jugador1+=1
            return f"JUEGO TERMINADO - Ronda {ronda2}\n¡Gana J1 - jugador1!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"
        elif jugador1 > 21: # Si el jugador1 se pasa gana el jugador2
            rondas_ganadas_jugador2+=1
            return f"JUEGO TERMINADO - Ronda {ronda2}\n¡Gana J2 - jugador2!\nJ1 - {nombre} - {cartas_jugador} ({str(suma_cartas(cartas_jugador))})\nJ2 - {nombre2} - {cartas_jugador2} ({str(suma_cartas(cartas_jugador2))})"

def jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2, final): # Este bucle sirve para preguntar si se quiere jugar de nuevo y en caso de que sea S empezará las partidas de nuevo y en caso de que se N terminará el programa y se ejecutará la función final_juego
    """Pregunta si quieres volver a jugar, si la respuesta es que si, ejecuta la partida de nuevo, si es que no, llama a la función final_juego."""
    while final == 0:
        quiere_jugar_de_nuevo=input("¿quieres jugar de nuevo? (S/N)").upper() # Pregunta si quiere jugar de nuevo
        if quiere_jugar_de_nuevo == "S": # Si responde S se ejecuta
            system("cls")
            if tipo_partida == "1 jugador":
                return "jugar de nuevo 1"# Si el tipo de partida que se eligió es el 1 se ejecutará la función jugador1_partida() y comenzará de nuevo la partida para un solo jugador
                jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida,final)
            if tipo_partida == "2 jugadores": # Si el tipo de partida que se eligió es el 2 se ejecutará la función jugador2_partida() y comenzará de nuevo la partida para dos jugadores
                jugador2_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida,final)
        elif quiere_jugar_de_nuevo == "N": # Si responde N saldrá del bucle
            final = 1
        else: # Si no se responde ninguna de las dos respuestas anteriores dará un error y volverá a comenzar el bucle
            print("ERROR - INTRODUCE UN DIGITO VALIDO")
    final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2,final) # Una vez fuera del bucle se llama a al función final_juego()

def modo_de_juego (rondas_ganadas_jugador1,rondas_ganadas_jugador2):#esta funcion elige entre jugar un jugador o dos jugadores
    """Permite elegir entre los dos modos de juegos que tiene, 1 jugador contra la máquina o 2 jugadores."""
    system("cls")
    print("¿Cuántos jugadores vais a hacer?(1/2)")
    jugadores= input() # Variable jugadores, el usuario teclea cuantos jugadores van a jugar 
    if jugadores == "1":# Si se cumple entonces llama a una funcion(jugador1_menu()), y se configura la partida para un modo jugador
        tipo_partida= 1
        system("cls")
        print("Partida configurada para 1 jugador y la máquina")
        return "1 jugador" # Llama a la función nombres() para guardar el nombre del jugador 
    elif jugadores == "2":# Si se cumple entonces llama a una funcion(jugador2_menu()), y se configura la partida para modo dos jugadores
        tipo_partida= 2
        system("cls")
        print("Partida configurada para 2 jugadores")
        return "2 jugadores" # Llama a la función nombres() para guardar el nombre de los jugadores
    else:# Si se introduce un caracter erróneo da un mensaje de error, y llama a la función modo_de_juego() y vuelve a preguntar los modos de juego
        print('ERROR - Por favor, introduce solo el numero de las opciones, por ejemplo si quieres la opcion (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')#mejorar el mensaje de error para que tenga sentido algo de elige 1 de un solo jugador o 2 de dos jugadores 
        input()
        modo_de_juego(rondas_ganadas_jugador1,rondas_ganadas_jugador2)

def menu():
    """Menú del blackjack donde se podrá elegir entre ver las reglas del Blackjack o empezar a jugar al Blackjack."""
    # Esta función lo que hace es que tienes un pequeño menu donde poder elegir varias opciones en este caso puede elegir leer reglas o jugar partida
    rondas_ganadas_jugador1=0
    rondas_ganadas_jugador2=0
    # Borra la pantalla y ejecuta lo de abajo
    system("cls")
    print("Bienvenido al blackjack.\n¿Qué vas a querer hacer?\nElige una opción:\n(1) Leer las reglas\n(2) Jugar al Blackjack")
    opcion= input() # Variable jugadores, el usuario teclea cuantos jugadores van a jugar
    if opcion == "1": # Si se cumple entonces llama a una funcion(jugador1_menu()), y se configura la partida para este modo 
        return "reglas"
    elif opcion == "2": # Si se cumple entonces llama a una función(modo_de_juego()), y se abre una pantalla donde eliges los jugadores 
        system("cls")
        return "modo de juego"
    else: # Da un mensaje de error, y empieza de nuevo la función correspondiente
        print('ERROR - Por favor, introduce solo el número de las opciones, por ejemplo si quieres la opción (1) leer las reglas, escribe "1" sin las comillas -\nPULSA ENTER PARA EMPEZAR DE NUEVO')
        input()
        menu()

def main(): # Llama a la función menu y comienza el programa
    """Es la función principal que desencadena el programa."""
    programa ="S"
    final=0
    while programa == "S":
        nombre = "nico"
        nombre2 ="ivan"
        modo_menu = "nada"
        rondas_ganadas_jugador1=0
        rondas_ganadas_jugador2=0
        tipo_partida=0
        menus="S"
        while menus=="S":
            modo_menu = menu()
            if modo_menu == "reglas":
                reglas()
            if modo_menu == "modo de juego":
                tipo_partida = modo_de_juego(rondas_ganadas_jugador1,rondas_ganadas_jugador2)
                menus = "N"
        
        partida ="S"
        if tipo_partida == "1 jugador":
            nombre= nombres(tipo_partida)
            nombre2= nombres2(tipo_partida)
            while partida == "S":
                rondas_ganadas_jugador1,rondas_ganadas_jugador2,cartas_jugador,cartas_jugador2,ronda2=jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida,final)
                print(se_pasa(cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2)) # Al salir del bucle se comprobará si las cartas del jugador o de la máquina se han pasado 
                input("Pulsa enter para ver los resultados")
                print(resultado(rondas_ganadas_jugador1, rondas_ganadas_jugador2,cartas_jugador2,cartas_jugador,ronda2, nombre, nombre2,tipo_partida,final)) # Una vez la rondas terminadas se llama a la función resultado() para imprimir los resultados de la partida
                partida = jugar_de_nuevo(rondas_ganadas_jugador1, rondas_ganadas_jugador2, tipo_partida,nombre,nombre2, final)
                if partida == "jugar de nuevo 1":
                    jugador1_partida(rondas_ganadas_jugador1,rondas_ganadas_jugador2, nombre,nombre2,tipo_partida,final)
                final_juego(rondas_ganadas_jugador1, rondas_ganadas_jugador2,nombre,nombre2,final)
        elif tipo_partida == "2 jugadores":
            nombre,nombre2= nombres(tipo_partida)
            while partida == "S":
                print("que no de error el codigo ")
        

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